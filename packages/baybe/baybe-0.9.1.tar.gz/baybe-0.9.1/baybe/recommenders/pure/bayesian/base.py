"""Base class for all Bayesian recommenders."""

from abc import ABC
from typing import Optional

import pandas as pd
from attrs import define, field

from baybe.acquisition.acqfs import qExpectedImprovement
from baybe.acquisition.base import AcquisitionFunction
from baybe.acquisition.utils import convert_acqf
from baybe.exceptions import DeprecationError
from baybe.recommenders.pure.base import PureRecommender
from baybe.searchspace import SearchSpace
from baybe.surrogates import _ONNX_INSTALLED, GaussianProcessSurrogate
from baybe.surrogates.base import Surrogate
from baybe.utils.dataframe import to_tensor

if _ONNX_INSTALLED:
    from baybe.surrogates import CustomONNXSurrogate


@define
class BayesianRecommender(PureRecommender, ABC):
    """An abstract class for Bayesian Recommenders."""

    surrogate_model: Surrogate = field(factory=GaussianProcessSurrogate)
    """The used surrogate model."""

    acquisition_function: AcquisitionFunction = field(
        converter=convert_acqf, factory=qExpectedImprovement, kw_only=True
    )
    """The used acquisition function class."""

    _botorch_acqf = field(default=None, init=False)
    """The current acquisition function."""

    acquisition_function_cls: bool = field(default=None)
    "Deprecated! Raises an error when used."

    @acquisition_function_cls.validator
    def _validate_deprecated_argument(self, _, value) -> None:
        """Raise DeprecationError if old acquisition_function_cls parameter is used."""
        if value is not None:
            raise DeprecationError(
                "Passing 'acquisition_function_cls' to the constructor is deprecated. "
                "The parameter has been renamed to 'acquisition_function'."
            )

    def _setup_botorch_acqf(
        self,
        searchspace: SearchSpace,
        train_x: Optional[pd.DataFrame] = None,
        train_y: Optional[pd.DataFrame] = None,
    ) -> None:
        """Create the current acquisition function from provided training data.

        The acquisition function is stored in the private attribute
        ``_acquisition_function``.

        Args:
            searchspace: The search space in which the experiments are to be conducted.
            train_x: The features of the conducted experiments.
            train_y: The corresponding response values.

        Raises:
            NotImplementedError: If the setup is attempted from empty training data
        """
        if train_x is None or train_y is None:
            raise NotImplementedError(
                "Bayesian recommenders do not support empty training data yet."
            )

        surrogate_model = self._fit(searchspace, train_x, train_y)
        self._botorch_acqf = self.acquisition_function.to_botorch(
            surrogate_model, train_x, train_y
        )

    def _fit(
        self,
        searchspace: SearchSpace,
        train_x: pd.DataFrame,
        train_y: pd.DataFrame,
    ) -> Surrogate:
        """Train a fresh surrogate model instance.

        Args:
            searchspace: The search space.
            train_x: The features of the conducted experiments.
            train_y: The corresponding response values.

        Returns:
            A surrogate model fitted to the provided data.

        Raises:
            ValueError: If the training inputs and targets do not have the same index.
        """
        # validate input
        if not train_x.index.equals(train_y.index):
            raise ValueError("Training inputs and targets must have the same index.")

        self.surrogate_model.fit(searchspace, *to_tensor(train_x, train_y))

        return self.surrogate_model

    def recommend(  # noqa: D102
        self,
        searchspace: SearchSpace,
        batch_size: int = 1,
        train_x: Optional[pd.DataFrame] = None,
        train_y: Optional[pd.DataFrame] = None,
    ) -> pd.DataFrame:
        # See base class.

        if _ONNX_INSTALLED and isinstance(self.surrogate_model, CustomONNXSurrogate):
            CustomONNXSurrogate.validate_compatibility(searchspace)

        self._setup_botorch_acqf(searchspace, train_x, train_y)

        return super().recommend(searchspace, batch_size, train_x, train_y)
