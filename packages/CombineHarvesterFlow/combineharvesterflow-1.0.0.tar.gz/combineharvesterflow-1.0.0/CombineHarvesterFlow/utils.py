from collections.abc import Callable

import equinox as eqx
import jax.numpy as jnp
import jax.random as jr
import numpy as np
import optax
from flowjax import wrappers
from flowjax.distributions import AbstractDistribution
from flowjax.train.train_utils import (count_fruitless, get_batches, step,
                                       train_val_split)
from flowjax.wrappers import unwrap
from jaxtyping import Array, ArrayLike, Float, PRNGKeyArray, PyTree
from tqdm import tqdm


def fit_to_data_weight(
    key: PRNGKeyArray,
    dist: PyTree,  # Custom losses may support broader types than AbstractDistribution
    x: ArrayLike,
    *,
    condition: ArrayLike | None = None,
    loss_fn: Callable | None = None,
    max_epochs: int = 100,
    max_patience: int = 5,
    batch_size: int = 100,
    val_prop: float = 0.1,
    learning_rate: float = 5e-4,
    optimizer: optax.GradientTransformation | None = None,
    return_best: bool = True,
    show_progress: bool = True,
    weights: ArrayLike | None = None
):
    r"""Train a distribution (e.g. a flow) to samples from the target distribution.

    The distribution can be unconditional :math:`p(x)` or conditional
    :math:`p(x|\text{condition})`. Note that the last batch in each epoch is dropped
    if truncated (to avoid recompilation). This function can also be used to fit
    non-distribution pytrees as long as a compatible loss function is provided.

    Args:
        key: Jax random seed.
        dist: The distribution to train.
        x: Samples from target distribution.
        condition: Conditioning variables. Defaults to None.
        loss_fn: Loss function. Defaults to MaximumLikelihoodLoss.
        max_epochs: Maximum number of epochs. Defaults to 100.
        max_patience: Number of consecutive epochs with no validation loss improvement
            after which training is terminated. Defaults to 5.
        batch_size: Batch size. Defaults to 100.
        val_prop: Proportion of data to use in validation set. Defaults to 0.1.
        learning_rate: Adam learning rate. Defaults to 5e-4.
        optimizer: Optax optimizer. If provided, this overrides the default Adam
            optimizer, and the learning_rate is ignored. Defaults to None.
        return_best: Whether the result should use the parameters where the minimum loss
            was reached (when True), or the parameters after the last update (when
            False). Defaults to True.
        show_progress: Whether to show progress bar. Defaults to True.

    Returns:
        A tuple containing the trained distribution and the losses.
    """
    # data = (x,) if condition is None else (x, condition)
    data = tuple(jnp.asarray(a) for a in (np.c_[x, weights],))

    if optimizer is None:
        optimizer = optax.adam(learning_rate)

    if loss_fn is None:
        loss_fn = WeightedMaximumLikelihoodLoss()

    params, static = eqx.partition(
        dist,
        eqx.is_inexact_array,
        is_leaf=lambda leaf: isinstance(leaf, wrappers.NonTrainable),
    )
    best_params = params
    opt_state = optimizer.init(params)

    # train val split
    key, subkey = jr.split(key)
    train_data, val_data = train_val_split(subkey, data, val_prop=val_prop)
    losses = {"train": [], "val": []}

    loop = tqdm(range(max_epochs), disable=not show_progress)

    for _ in loop:
        # Shuffle data
        key, *subkeys = jr.split(key, 3)
        train_data = [jr.permutation(subkeys[0], a) for a in train_data]
        val_data = [jr.permutation(subkeys[1], a) for a in val_data]

        # Train epoch
        batch_losses = []
        for batch in zip(*get_batches(train_data, batch_size), strict=True):
            params, opt_state, loss_i = step(
                params,
                static,
                batch[0][:, :-1], batch[0][:, -1],
                optimizer=optimizer,
                opt_state=opt_state,
                loss_fn=loss_fn,
            )
            batch_losses.append(loss_i)
        losses["train"].append(sum(batch_losses) / len(batch_losses))

        # Val epoch
        batch_losses = []
        for batch in zip(*get_batches(val_data, batch_size), strict=True):
            loss_i = loss_fn(params, static, batch[0][:, :-1], batch[0][:, -1])
            batch_losses.append(loss_i)
        losses["val"].append(sum(batch_losses) / len(batch_losses))

        loop.set_postfix({k: v[-1] for k, v in losses.items()})
        if losses["val"][-1] == min(losses["val"]):
            best_params = params

        elif count_fruitless(losses["val"]) > max_patience:
            loop.set_postfix_str(f"{loop.postfix} (Max patience reached)")
            break

    params = best_params if return_best else params
    dist = eqx.combine(params, static)
    return dist, losses


class WeightedMaximumLikelihoodLoss:
    @eqx.filter_jit
    def __call__(
        self,
        params: AbstractDistribution,
        static: AbstractDistribution,
        x: Array, weights: Array,
        condition: Array | None = None,
    ) -> Float[Array, ""]:
        """Compute the loss."""

        dist = unwrap(eqx.combine(params, static))
        evl = -dist.log_prob(x, condition)
        return (evl*weights).sum()/len(evl)
