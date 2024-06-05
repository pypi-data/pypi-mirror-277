"""BayBE surrogates."""

from baybe.surrogates.custom import _ONNX_INSTALLED, register_custom_architecture
from baybe.surrogates.gaussian_process.core import GaussianProcessSurrogate
from baybe.surrogates.linear import BayesianLinearSurrogate
from baybe.surrogates.naive import MeanPredictionSurrogate
from baybe.surrogates.ngboost import NGBoostSurrogate
from baybe.surrogates.random_forest import RandomForestSurrogate

__all__ = [
    "register_custom_architecture",
    "BayesianLinearSurrogate",
    "GaussianProcessSurrogate",
    "MeanPredictionSurrogate",
    "NGBoostSurrogate",
    "RandomForestSurrogate",
]

if _ONNX_INSTALLED:
    from baybe.surrogates.custom import CustomONNXSurrogate  # noqa: F401

    __all__.append("CustomONNXSurrogate")
