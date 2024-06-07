"""Module which contains Exponential model class"""

import numpy as np
from scipy.stats import expon

from mpest.types import Samples, Params
from mpest.models.abstract_model import AModelDifferentiable, AModelWithGenerator


class ExponentialModel(AModelDifferentiable, AModelWithGenerator):
    """
    f(x) = l * e^(-lx)

    l = e^(_l)

    O = [_l]
    """

    @property
    def name(self) -> str:
        return "Exponential"

    def params_convert_to_model(self, params: Params) -> Params:
        return np.log(params)

    def params_convert_from_model(self, params: Params) -> Params:
        return np.exp(params)

    def generate(self, params: Params, size: int = 1) -> Samples:
        return np.array(expon.rvs(scale=1 / params[0], size=size))

    def pdf(self, x: float, params: Params) -> float:
        if x < 0:
            return 0
        (l,) = params
        return np.exp(l - np.exp(l) * x)

    def lpdf(self, x: float, params: Params) -> float:
        if x < 0:
            return -np.inf
        (l,) = params
        return l - np.exp(l) * x

    def ldl(self, x: float, params: Params) -> float:
        """Method which returns logarithm of derivative with respect to parameter l"""

        if x < 0:
            return -np.inf
        (l,) = params
        return 1 - np.exp(l) * x

    def ld_params(self, x: float, params: Params) -> np.ndarray:
        return np.array([self.ldl(x, params)])
