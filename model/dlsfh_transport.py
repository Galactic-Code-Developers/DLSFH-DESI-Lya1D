"""DLSFH phenomenological transport operator.

This module defines the canonical minimal ansatz used in the paper:
  T(k,z) = exp[-Xi(z) k^2], with Xi(z)=Xi0 * a(z)^2.

In the matter power spectrum:
  P_m(k,z) -> exp[-2 Xi(z) k^2] P_m(k,z)
"""
import numpy as np

def a_of_z(z: float) -> float:
    return 1.0 / (1.0 + z)

def Xi_of_z(z: float, Xi0: float, alpha: float = 1.0) -> float:
    a = a_of_z(z)
    return Xi0 * (a ** (2.0 * alpha))

def suppression_factor(k: np.ndarray, z: float, Xi0: float, alpha: float = 1.0) -> np.ndarray:
    """Return exp[-2 Xi(z) k^2]. k in h/Mpc, Xi0 in (Mpc/h)^2."""
    Xi = Xi_of_z(z, Xi0, alpha=alpha)
    return np.exp(-2.0 * Xi * (k ** 2))
