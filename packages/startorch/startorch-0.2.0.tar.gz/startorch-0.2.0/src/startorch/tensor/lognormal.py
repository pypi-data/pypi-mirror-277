r"""Contain the implementation of tensor generators where the values are
sampled from a Log-Normal distribution."""

from __future__ import annotations

__all__ = [
    "LogNormalTensorGenerator",
    "RandLogNormalTensorGenerator",
    "RandTruncLogNormalTensorGenerator",
    "TruncLogNormalTensorGenerator",
]

from typing import TYPE_CHECKING

from coola.utils.format import str_indent, str_mapping

from startorch.random import (
    log_normal,
    rand_log_normal,
    rand_trunc_log_normal,
    trunc_log_normal,
)
from startorch.tensor.base import BaseTensorGenerator, setup_tensor_generator

if TYPE_CHECKING:
    import torch


class LogNormalTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    log-Normal distribution.

    Args:
        mean: A tensor generator (or its configuration) to
            generate the mean of the underlying Normal distribution.
        std: A tensor generator (or its configuration) to
            generate the standard deviation of the underlying Normal
            distribution.

    Example usage:

    ```pycon

    >>> from startorch.tensor import LogNormal, RandUniform
    >>> generator = LogNormal(
    ...     mean=RandUniform(low=-1.0, high=1.0), std=RandUniform(low=1.0, high=2.0)
    ... )
    >>> generator
    LogNormalTensorGenerator(
      (mean): RandUniformTensorGenerator(low=-1.0, high=1.0)
      (std): RandUniformTensorGenerator(low=1.0, high=2.0)
    )
    >>> generator.generate(size=(2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, mean: BaseTensorGenerator | dict, std: BaseTensorGenerator | dict) -> None:
        super().__init__()
        self._mean = setup_tensor_generator(mean)
        self._std = setup_tensor_generator(std)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"mean": self._mean, "std": self._std}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return log_normal(
            mean=self._mean.generate(size=size, rng=rng),
            std=self._std.generate(size=size, rng=rng),
            generator=rng,
        )


class RandLogNormalTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    log-Normal distribution.

    Args:
        mean: The mean of the underlying Normal distribution.
        std: The standard deviation of the underlying Normal
            distribution.

    Raises:
        ValueError: if ``std`` is not a positive number.

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandLogNormal
    >>> generator = RandLogNormal(mean=0.0, std=1.0)
    >>> generator
    RandLogNormalTensorGenerator(mean=0.0, std=1.0)
    >>> generator.generate(size=(2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, mean: float = 0.0, std: float = 1.0) -> None:
        super().__init__()
        self._mean = float(mean)
        if std <= 0:
            msg = f"std has to be greater than 0 (received: {std})"
            raise ValueError(msg)
        self._std = float(std)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(mean={self._mean}, std={self._std})"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return rand_log_normal(
            size=size,
            mean=self._mean,
            std=self._std,
            generator=rng,
        )


class RandTruncLogNormalTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator to generate cyclic tensors by
    sampling values from a truncated log-Normal distribution.

    Args:
        mean: The mean of the log-Normal distribution.
        std: The standard deviation of the log-Normal
            distribution.
        min_value: The minimum value.
        max_value: The maximum value.

    Raises:
        ValueError: if ``std`` is not a positive number.
        ValueError: if ``max_value`` is lower than ``min_value``.

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandTruncLogNormal
    >>> generator = RandTruncLogNormal(mean=0.0, std=1.0, min_value=0.0, max_value=1.0)
    >>> generator
    RandTruncLogNormalTensorGenerator(mean=0.0, std=1.0, min_value=0.0, max_value=1.0)
    >>> generator.generate(size=(2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self, mean: float = 0.0, std: float = 1.0, min_value: float = 0.0, max_value: float = 5.0
    ) -> None:
        super().__init__()
        self._mean = float(mean)
        if std <= 0:
            msg = f"std has to be greater than 0 (received: {std})"
            raise ValueError(msg)
        self._std = float(std)
        if max_value < min_value:
            msg = f"max_value ({max_value}) has to be greater or equal to min_value ({min_value})"
            raise ValueError(msg)
        self._min_value = float(min_value)
        self._max_value = float(max_value)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(mean={self._mean}, std={self._std}, "
            f"min_value={self._min_value}, max_value={self._max_value})"
        )

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return rand_trunc_log_normal(
            size=size,
            mean=self._mean,
            std=self._std,
            min_value=self._min_value,
            max_value=self._max_value,
            generator=rng,
        )


class TruncLogNormalTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    truncated log-Normal distribution.

    Args:
        mean: A tensor generator (or its configuration) to
            generate the mean of the underlying Normal distribution.
        std: A tensor generator (or its configuration) to
            generate the standard deviation of the underlying Normal
            distribution.
        min_value: A tensor generator (or its configuration)
            to generate the minimum value (included).
        max_value: A tensor generator (or its configuration)
            to generate the maximum value (excluded).

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandUniform, TruncLogNormal
    >>> generator = TruncLogNormal(
    ...     mean=RandUniform(low=-1.0, high=1.0),
    ...     std=RandUniform(low=1.0, high=2.0),
    ...     min_value=RandUniform(low=0.0, high=2.0),
    ...     max_value=RandUniform(low=5.0, high=10.0),
    ... )
    >>> generator
    TruncLogNormalTensorGenerator(
      (mean): RandUniformTensorGenerator(low=-1.0, high=1.0)
      (std): RandUniformTensorGenerator(low=1.0, high=2.0)
      (min_value): RandUniformTensorGenerator(low=0.0, high=2.0)
      (max_value): RandUniformTensorGenerator(low=5.0, high=10.0)
    )
    >>> generator.generate(size=(2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        mean: BaseTensorGenerator | dict,
        std: BaseTensorGenerator | dict,
        min_value: BaseTensorGenerator | dict,
        max_value: BaseTensorGenerator | dict,
    ) -> None:
        super().__init__()
        self._mean = setup_tensor_generator(mean)
        self._std = setup_tensor_generator(std)
        self._min_value = setup_tensor_generator(min_value)
        self._max_value = setup_tensor_generator(max_value)

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "mean": self._mean,
                    "std": self._std,
                    "min_value": self._min_value,
                    "max_value": self._max_value,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return trunc_log_normal(
            mean=self._mean.generate(size=size, rng=rng),
            std=self._std.generate(size=size, rng=rng),
            min_value=self._min_value.generate(size=size, rng=rng),
            max_value=self._max_value.generate(size=size, rng=rng),
            generator=rng,
        )
