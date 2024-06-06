"""Symfc API."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Optional, Union

import numpy as np

from symfc.basis_sets import FCBasisSetBase, FCBasisSetO2, FCBasisSetO3
from symfc.solvers import FCSolverO2, FCSolverO2O3
from symfc.utils.utils import SymfcAtoms


class Symfc:
    """Symfc API."""

    def __init__(
        self,
        supercell: SymfcAtoms,
        displacements: Optional[np.ndarray] = None,
        forces: Optional[np.ndarray] = None,
        use_mkl: bool = False,
        log_level: int = 0,
    ):
        """Init method."""
        self._supercell: SymfcAtoms = supercell
        self._displacements: Optional[np.ndarray] = displacements
        self._forces: Optional[np.ndarray] = forces
        self._use_mkl = use_mkl
        self._log_level = log_level

        self._basis_set: dict[FCBasisSetBase] = {}
        self._force_constants: dict[np.ndarray] = {}

    @property
    def basis_set(self) -> dict[FCBasisSetBase]:
        """Return basis set instance.

        Returns
        -------
        dict[FCBasisSet]
            The key is the order of basis set in int.

        """
        return self._basis_set

    @property
    def force_constants(self) -> dict[np.ndarray]:
        """Return force constants.

        Returns
        -------
        dict[np.ndarray]
            The key is the order of force_constants in int.

        """
        return self._force_constants

    @property
    def displacements(self) -> np.ndarray:
        """Setter and getter of supercell displacements.

        ndarray
            shape=(n_snapshot, natom, 3), dtype='double', order='C'

        """
        return self._displacements

    @displacements.setter
    def displacements(self, displacements: Union[np.ndarray, list, tuple]):
        self._displacements = np.array(displacements, dtype="double", order="C")

    @property
    def forces(self) -> np.ndarray:
        """Setter and getter of supercell forces.

        ndarray
            shape=(n_snapshot, natom, 3), dtype='double', order='C'

        """
        return self._forces

    @forces.setter
    def forces(self, forces: Union[np.ndarray, list, tuple]):
        self._forces = np.array(forces, dtype="double", order="C")

    def run(self, orders: Sequence[int], is_compact_fc=True) -> Symfc:
        """Run basis set and force constants calculation."""
        if (
            orders is not None
            and self._displacements is not None
            and self._forces is not None
        ):
            for order in orders:
                self._compute_basis_set(order)
            self.solve(orders, is_compact_fc=is_compact_fc)
        return self

    def solve(self, orders: Sequence[int], is_compact_fc=True) -> Symfc:
        """Calculate force constants.

        orders : Sequence[int]
            Sequence of fc orders.

        """
        self._check_dataset()
        for order in orders:
            if order not in (2, 3):
                raise NotImplementedError("Only order-2 and order-3 are implemented.")
            if order == 2:
                basis_set: FCBasisSetO2 = self._basis_set[2]
                solver_o2 = FCSolverO2(
                    basis_set,
                    use_mkl=self._use_mkl,
                    log_level=self._log_level,
                ).solve(self._displacements, self._forces)
                if is_compact_fc:
                    self._force_constants[2] = solver_o2.compact_fc
                else:
                    self._force_constants[2] = solver_o2.full_fc
            if order == 3:
                basis_set_o2: FCBasisSetO2 = self._basis_set[2]
                basis_set_o3: FCBasisSetO3 = self._basis_set[3]
                solver_o2o3 = FCSolverO2O3(
                    [basis_set_o2, basis_set_o3],
                    use_mkl=self._use_mkl,
                    log_level=self._log_level,
                ).solve(self._displacements, self._forces)
                if is_compact_fc:
                    fc2, fc3 = solver_o2o3.compact_fc
                else:
                    fc2, fc3 = solver_o2o3.full_fc
                self._force_constants[2] = fc2
                self._force_constants[3] = fc3
        return self

    def _compute_basis_set(self, order: int):
        """Set order of force constants."""
        if order not in (2, 3):
            raise NotImplementedError("Only fc2 basis set is implemented.")

        if order == 2:
            basis_set_o2 = FCBasisSetO2(
                self._supercell, use_mkl=self._use_mkl, log_level=self._log_level
            ).run()
            self._basis_set[2] = basis_set_o2
        if order == 3:
            basis_set_o3 = FCBasisSetO3(
                self._supercell, use_mkl=self._use_mkl, log_level=self._log_level
            ).run()
            self._basis_set[3] = basis_set_o3

    def _check_dataset(self):
        if self._displacements is None:
            raise RuntimeError("Dispalcements not found.")
        if self._forces is None:
            raise RuntimeError("Forces not found.")
        if self._displacements.shape != self._forces.shape:
            raise RuntimeError("Shape mismatch between dispalcements and forces.")
        if self._displacements.shape != self._forces.shape:
            raise RuntimeError("Shape mismatch between dispalcements and forces.")
        if self._displacements.ndim != 3 or self._displacements.shape[1:] != (
            len(self._supercell),
            3,
        ):
            raise RuntimeError(
                "Inconsistent array shape of displacements "
                f"{self._displacements.shape} with respect to supercell "
                f"{len(self._supercell)}."
            )
        if self._forces.ndim != 3 or self._forces.shape[1:] != (
            len(self._supercell),
            3,
        ):
            raise RuntimeError(
                "Inconsistent array shape of forces "
                f"{self._forces.shape} with respect to supercell "
                f"{len(self._supercell)}."
            )
