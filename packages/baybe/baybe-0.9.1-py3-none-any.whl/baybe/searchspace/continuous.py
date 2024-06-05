"""Continuous subspaces."""

from __future__ import annotations

from collections.abc import Collection, Sequence
from typing import Any, Optional, cast

import numpy as np
import pandas as pd
from attr import define, field

from baybe.constraints import (
    ContinuousLinearEqualityConstraint,
    ContinuousLinearInequalityConstraint,
)
from baybe.parameters import NumericalContinuousParameter
from baybe.parameters.base import ContinuousParameter
from baybe.parameters.utils import get_parameters_from_dataframe
from baybe.searchspace.validation import validate_parameter_names
from baybe.serialization import SerialMixin, converter, select_constructor_hook
from baybe.utils.basic import to_tuple
from baybe.utils.dataframe import pretty_print_df
from baybe.utils.numerical import DTypeFloatNumpy


@define
class SubspaceContinuous(SerialMixin):
    """Class for managing continuous subspaces.

    Builds the subspace from parameter definitions, keeps
    track of search metadata, and provides access to candidate sets and different
    parameter views.
    """

    parameters: tuple[NumericalContinuousParameter, ...] = field(
        converter=to_tuple, validator=lambda _, __, x: validate_parameter_names(x)
    )
    """The list of parameters of the subspace."""

    constraints_lin_eq: tuple[ContinuousLinearEqualityConstraint, ...] = field(
        converter=to_tuple, factory=tuple
    )
    """List of linear equality constraints."""

    constraints_lin_ineq: tuple[ContinuousLinearInequalityConstraint, ...] = field(
        converter=to_tuple, factory=tuple
    )
    """List of linear inequality constraints."""

    def __str__(self) -> str:
        if self.is_empty:
            return ""

        start_bold = "\033[1m"
        end_bold = "\033[0m"

        # Convert the lists to dataFrames to be able to use pretty_printing
        param_list = [param.summary() for param in self.parameters]
        eq_constraints_list = [constr.summary() for constr in self.constraints_lin_eq]
        ineq_constraints_list = [
            constr.summary() for constr in self.constraints_lin_ineq
        ]
        param_df = pd.DataFrame(param_list)
        lin_eq_constr_df = pd.DataFrame(eq_constraints_list)
        lin_ineq_constr_df = pd.DataFrame(ineq_constraints_list)

        # Put all attributes of the continuous class in one string
        continuous_str = f"""{start_bold}Continuous Search Space{end_bold}
            \n{start_bold}Continuous Parameters{end_bold}\n{pretty_print_df(param_df)}
            \n{start_bold}List of Linear Equality Constraints{end_bold}
            \r{pretty_print_df(lin_eq_constr_df)}
            \n{start_bold}List of Linear Inequality Constraints{end_bold}
            \r{pretty_print_df(lin_ineq_constr_df)}"""

        return continuous_str.replace("\n", "\n ").replace("\r", "\r ")

    @classmethod
    def empty(cls) -> SubspaceContinuous:
        """Create an empty continuous subspace."""
        return SubspaceContinuous([])

    @classmethod
    def from_bounds(cls, bounds: pd.DataFrame) -> SubspaceContinuous:
        """Create a hyperrectangle-shaped continuous subspace with given bounds.

        Args:
            bounds: The bounds of the parameters.

        Returns:
            The constructed subspace.
        """
        # Assert that the input represents valid bounds
        assert bounds.shape[0] == 2
        assert (np.diff(bounds.values, axis=0) >= 0).all()
        assert bounds.apply(pd.api.types.is_numeric_dtype).all()

        # Create the corresponding parameters and from them the search space
        parameters = [
            NumericalContinuousParameter(cast(str, name), bound)
            for (name, bound) in bounds.items()
        ]
        return SubspaceContinuous(parameters)

    @classmethod
    def from_dataframe(
        cls,
        df: pd.DataFrame,
        parameters: Optional[Sequence[ContinuousParameter]] = None,
    ) -> SubspaceContinuous:
        """Create a hyperrectangle-shaped continuous subspace from a dataframe.

        More precisely, create the smallest axis-aligned hyperrectangle-shaped
        continuous subspace that contains the points specified in the given dataframe.

        Args:
            df: The dataframe specifying the points spanning the subspace.
            parameters: Optional parameter objects corresponding to the columns in the
                given dataframe that can be provided to explicitly control parameter
                attributes. If a match between column name and parameter name is found,
                the corresponding parameter object is used. If a column has no match in
                the parameter list, a new
                :class:`baybe.parameters.numerical.NumericalContinuousParameter`
                is created with default optional arguments. For more details, see
                :func:`baybe.parameters.utils.get_parameters_from_dataframe`.

        Raises:
            ValueError: If parameter types other than
                :class:`baybe.parameters.numerical.NumericalContinuousParameter`
                are provided.

        Returns:
            The created continuous subspace.
        """
        # TODO: Add option for convex hull once constraints are in place

        if parameters and not all(
            isinstance(p, NumericalContinuousParameter) for p in parameters
        ):
            raise ValueError(
                "Currently, only parameters of type "
                "'{NumericalContinuousParameter.__name__}' are supported."
            )

        def continuous_parameter_factory(name: str, values: Collection[Any]):
            return NumericalContinuousParameter(name, (min(values), max(values)))

        # Get the full list of both explicitly and implicitly defined parameter
        parameters = get_parameters_from_dataframe(
            df, continuous_parameter_factory, parameters
        )

        return cls(parameters)

    @property
    def is_empty(self) -> bool:
        """Return whether this subspace is empty."""
        return len(self.parameters) == 0

    @property
    def param_names(self) -> tuple[str, ...]:
        """Return list of parameter names."""
        return tuple(p.name for p in self.parameters)

    @property
    def param_bounds_comp(self) -> np.ndarray:
        """Return bounds as numpy array."""
        if not self.parameters:
            return np.empty((2, 0), dtype=DTypeFloatNumpy)
        return np.stack([p.bounds.to_ndarray() for p in self.parameters]).T

    def transform(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """See :func:`baybe.searchspace.discrete.SubspaceDiscrete.transform`.

        Args:
            data: The data that should be transformed.

        Returns:
            The transformed data.
        """
        # Transform continuous parameters
        comp_rep = data[[p.name for p in self.parameters]]

        return comp_rep

    def samples_random(self, n_points: int = 1) -> pd.DataFrame:
        """Get random point samples from the continuous space.

        Args:
            n_points: Number of points that should be sampled.

        Returns:
            A data frame containing the points as rows with columns corresponding to the
            parameter names.
        """
        if not self.parameters:
            return pd.DataFrame()
        import torch
        from botorch.utils.sampling import get_polytope_samples

        # TODO Revisit: torch and botorch here are actually only necessary if there
        # are constraints. If there are none and the lists are empty we can just sample
        # without the get_polytope_samples, which means torch and botorch
        # wouldn't be needed.

        points = get_polytope_samples(
            n=n_points,
            bounds=torch.from_numpy(self.param_bounds_comp),
            equality_constraints=[
                c.to_botorch(self.parameters) for c in self.constraints_lin_eq
            ],
            inequality_constraints=[
                c.to_botorch(self.parameters) for c in self.constraints_lin_ineq
            ],
        )

        return pd.DataFrame(points, columns=self.param_names)

    def samples_full_factorial(self, n_points: int = 1) -> pd.DataFrame:
        """Get random point samples from the full factorial of the continuous space.

        Args:
            n_points: Number of points that should be sampled.

        Returns:
            A data frame containing the points as rows with columns corresponding to the
            parameter names.

        Raises:
            ValueError: If there are not enough points to sample from.
        """
        full_factorial = self.full_factorial

        if len(full_factorial) < n_points:
            raise ValueError(
                f"You are trying to sample {n_points} points from the full factorial of"
                f" the continuous space bounds, but it has only {len(full_factorial)} "
                f"points."
            )

        return full_factorial.sample(n=n_points).reset_index(drop=True)

    @property
    def full_factorial(self) -> pd.DataFrame:
        """Get the full factorial of the continuous space."""
        index = pd.MultiIndex.from_product(
            self.param_bounds_comp.T.tolist(), names=self.param_names
        )

        return pd.DataFrame(index=index).reset_index()


# Register deserialization hook
converter.register_structure_hook(SubspaceContinuous, select_constructor_hook)
