r"""Contain functions to sample values from discrete uni-variate
distributions supported on a bounded interval."""

from __future__ import annotations

__all__ = ["rand_poisson"]


import torch


def rand_poisson(
    size: list[int] | tuple[int, ...],
    rate: float = 1.0,
    generator: torch.Generator | None = None,
) -> torch.Tensor:
    r"""Create a tensor filled with values sampled from a Poisson
    distribution.

    Args:
        size: The tensor shape.
        rate: The rate of the Poisson distribution.
            This value has to be greater than 0.
        generator: An optional random generator.

    Returns:
        ``torch.Tensor`` of type float: A tensor filled with values
            sampled from a Poisson distribution.

    Raises:
        ValueError: if the ``rate`` parameter is not valid.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.random import rand_poisson
    >>> rand_poisson(size=(2, 3), rate=2.0)
    tensor([...])

    ```
    """
    if rate <= 0:
        msg = f"rate has to be greater than 0 (received: {rate})"
        raise ValueError(msg)
    return torch.poisson(torch.full(size, rate, dtype=torch.float), generator=generator)
