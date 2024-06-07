r"""Contain the implementation of sequence generators where the values
are sampled from a Cauchy distribution."""

from __future__ import annotations

__all__ = [
    "CauchySequenceGenerator",
    "RandCauchySequenceGenerator",
    "RandTruncCauchySequenceGenerator",
    "TruncCauchySequenceGenerator",
]

from typing import TYPE_CHECKING

from coola.utils.format import str_indent, str_mapping

from startorch.random import cauchy, rand_cauchy, rand_trunc_cauchy, trunc_cauchy
from startorch.sequence.base import BaseSequenceGenerator, setup_sequence_generator
from startorch.utils.conversion import to_tuple

if TYPE_CHECKING:
    import torch


class CauchySequenceGenerator(BaseSequenceGenerator):
    r"""Implement a class to generate sequence by sampling values from a
    Cauchy distribution.

    Args:
        loc: A sequence generator (or its configuration) to
            generate the location.
        scale: A sequence generator (or its configuration)
            to generate the scale.

    Example usage:

    ```pycon

    >>> from startorch.sequence import Cauchy, RandUniform
    >>> generator = Cauchy(
    ...     loc=RandUniform(low=-1.0, high=1.0),
    ...     scale=RandUniform(low=1.0, high=2.0),
    ... )
    >>> generator
    CauchySequenceGenerator(
      (loc): RandUniformSequenceGenerator(low=-1.0, high=1.0, feature_size=(1,))
      (scale): RandUniformSequenceGenerator(low=1.0, high=2.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=6, batch_size=2)
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: BaseSequenceGenerator | dict,
        scale: BaseSequenceGenerator | dict,
    ) -> None:
        super().__init__()
        self._loc = setup_sequence_generator(loc)
        self._scale = setup_sequence_generator(scale)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"loc": self._loc, "scale": self._scale}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return cauchy(
            loc=self._loc.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            scale=self._scale.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            generator=rng,
        )


class RandCauchySequenceGenerator(BaseSequenceGenerator):
    r"""Implement a class to generate sequence by sampling values from a
    Cauchy distribution.

    Args:
        loc: The location/median of the Cauchy distribution.
        scale: The scale of the distribution.
        feature_size: The feature size.

    Raises:
        ValueError: if ``scale`` is not a positive number.

    Example usage:

    ```pycon

    >>> from startorch.sequence import RandCauchy
    >>> generator = RandCauchy(loc=0.0, scale=1.0)
    >>> generator
    RandCauchySequenceGenerator(loc=0.0, scale=1.0, feature_size=(1,))
    >>> generator.generate(seq_len=6, batch_size=2)
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: float = 0.0,
        scale: float = 1.0,
        feature_size: tuple[int, ...] | list[int] | int = 1,
    ) -> None:
        super().__init__()
        self._loc = float(loc)
        if scale <= 0:
            msg = f"scale has to be greater than 0 (received: {scale})"
            raise ValueError(msg)
        self._scale = float(scale)
        self._feature_size = to_tuple(feature_size)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(loc={self._loc}, scale={self._scale}, "
            f"feature_size={self._feature_size})"
        )

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return rand_cauchy(
            size=(batch_size, seq_len, *self._feature_size),
            loc=self._loc,
            scale=self._scale,
            generator=rng,
        )


class RandTruncCauchySequenceGenerator(BaseSequenceGenerator):
    r"""Implement a class to generate sequence by sampling values from a
    truncated Cauchy distribution.

    Args:
        loc: The location/median of the Cauchy distribution.
        scale: The scale of the distribution.
        min_value: The minimum value (included).
        max_value: The maximum value (excluded).
        feature_size: The feature size.

    Raises:
        ValueError: if ``std`` is not a positive number.
        ValueError: if ``max_value`` is lower than ``min_value``.

    Example usage:

    ```pycon

    >>> from startorch.sequence import RandTruncCauchy
    >>> generator = RandTruncCauchy(loc=0.0, scale=1.0, min_value=-5.0, max_value=5.0)
    >>> generator
    RandTruncCauchySequenceGenerator(loc=0.0, scale=1.0, min_value=-5.0, max_value=5.0, feature_size=(1,))
    >>> generator.generate(seq_len=6, batch_size=2)
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: float = 0.0,
        scale: float = 1.0,
        min_value: float = -2.0,
        max_value: float = 2.0,
        feature_size: tuple[int, ...] | list[int] | int = 1,
    ) -> None:
        super().__init__()
        self._loc = float(loc)
        if scale <= 0:
            msg = f"scale has to be greater than 0 (received: {scale})"
            raise ValueError(msg)
        self._scale = float(scale)
        if max_value < min_value:
            msg = f"max_value ({max_value}) has to be greater or equal to min_value ({min_value})"
            raise ValueError(msg)
        self._min_value = float(min_value)
        self._max_value = float(max_value)

        self._feature_size = to_tuple(feature_size)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(loc={self._loc}, scale={self._scale}, "
            f"min_value={self._min_value}, max_value={self._max_value}, "
            f"feature_size={self._feature_size})"
        )

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return rand_trunc_cauchy(
            size=(batch_size, seq_len, *self._feature_size),
            loc=self._loc,
            scale=self._scale,
            min_value=self._min_value,
            max_value=self._max_value,
            generator=rng,
        )


class TruncCauchySequenceGenerator(BaseSequenceGenerator):
    r"""Implement a class to generate sequence by sampling values from a
    Cauchy distribution.

    Args:
        loc: A sequence generator (or its configuration) to
            generate the location.
        scale: A sequence generator (or its configuration)
            to generate the scale.
        min_value: A sequence generator (or its
            configuration) to generate the minimum value (included).
        max_value: A sequence generator (or its
            configuration) to generate the  maximum value (excluded).

    Example usage:

    ```pycon

    >>> from startorch.sequence import RandUniform, TruncCauchy
    >>> generator = TruncCauchy(
    ...     loc=RandUniform(low=-1.0, high=1.0),
    ...     scale=RandUniform(low=1.0, high=2.0),
    ...     min_value=RandUniform(low=-10.0, high=-5.0),
    ...     max_value=RandUniform(low=5.0, high=10.0),
    ... )
    >>> generator
    TruncCauchySequenceGenerator(
      (loc): RandUniformSequenceGenerator(low=-1.0, high=1.0, feature_size=(1,))
      (scale): RandUniformSequenceGenerator(low=1.0, high=2.0, feature_size=(1,))
      (min_value): RandUniformSequenceGenerator(low=-10.0, high=-5.0, feature_size=(1,))
      (max_value): RandUniformSequenceGenerator(low=5.0, high=10.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=6, batch_size=2)
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: BaseSequenceGenerator | dict,
        scale: BaseSequenceGenerator | dict,
        min_value: BaseSequenceGenerator | dict,
        max_value: BaseSequenceGenerator | dict,
    ) -> None:
        super().__init__()
        self._loc = setup_sequence_generator(loc)
        self._scale = setup_sequence_generator(scale)
        self._min_value = setup_sequence_generator(min_value)
        self._max_value = setup_sequence_generator(max_value)

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "loc": self._loc,
                    "scale": self._scale,
                    "min_value": self._min_value,
                    "max_value": self._max_value,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return trunc_cauchy(
            loc=self._loc.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            scale=self._scale.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            min_value=self._min_value.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            max_value=self._max_value.generate(seq_len=seq_len, batch_size=batch_size, rng=rng),
            generator=rng,
        )
