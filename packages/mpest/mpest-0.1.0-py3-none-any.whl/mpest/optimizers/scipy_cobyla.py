"""Module which contains COBYLA optimizer"""

from typing import Callable
from scipy.optimize import minimize

from mpest.types import Params
from mpest.optimizers.abstract_optimizer import AOptimizer


class ScipyCOBYLA(AOptimizer):
    """Class which represents SciPy COBYLA optimizer"""

    @property
    def name(self):
        return "ScipyCOBYLA"

    def minimize(
        self,
        func: Callable[[Params], float],
        params: Params,
    ) -> Params:
        return minimize(func, params, method="COBYLA").x
