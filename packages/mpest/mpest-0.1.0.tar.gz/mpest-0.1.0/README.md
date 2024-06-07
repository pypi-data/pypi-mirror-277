![PyLint](https://github.com/ToxaKaz/EM-algo/actions/workflows/pylint.yml/badge.svg)
![Check code style](https://github.com/ToxaKaz/EM-algo/actions/workflows/code_style.yml/badge.svg)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
![Unit Tests](https://github.com/ToxaKaz/EM-algo/actions/workflows/test.yml/badge.svg)

## Abstract

This package contains realization of em algorithm for solving the parameter estimation of mixture distribution problem:

$$p(x | \Omega, F, \Theta) = \sum_{j=1}^k \omega_j f_j(x | \theta_j)$$

- $p(x | \Omega, F, \Theta)$ - mixture distribution
- $f_j(x | \theta_j) \in F$ - $j$ distribution
- $\omega_j \in \Omega$ - prior probability of $j$ distribution
- $\theta_j \in \Theta$ - parameters of $j$ distribution

The problem is to find $\Omega$ and $\Theta$ params of custom mixture distribution with known (or guessed) $k$, $F$ and guessed or randomized initial approximation.

This package uses EM algorithm tuned to work with different distributions models and optimizers, which could match the given interfaces. This allows using this package even for mixture distribution of different distributions classes. For example mixture distribution of both Gaussian and Exponential distributions.

## Usage

The package can work with mixture distribution of any combination of models, which implements `AModel` abstract class. EM algorithm result can be calculated by using `EM` class with `AOptimizer` implementation and guessed or random initial approximation.

Given samples should be wrapped in `MixtureDistribution` then by using `EM.solve` the result will be calculated. `EM` class depends on `TOptimizer`, `ABreakpointer` and `ADistributionChecker` objects. :
- `ABreakpointer` class $-$ the EM algorithm breakpointer function. There are few basic realizations of that abstract class in that package.
- `ADistributionChecker` class $-$ sometimes because of using math optimizers in M-step of EM algorithm, some distributions inside mixture distribution can become degenerated. Such distributions may be detected and removed from calculations. There are few basic realizations of that abstract class in that package.
- `AOptimizer`/`AOptimizerJacobian` classes $-$ math optimizers for M step of algorithm. There are few SciPy optimizers made follow the given interfaces.

### Code example

```Python
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from mpest import Distribution, MixtureDistribution, Problem
from mpest.models import WeibullModelExp, GaussianModel
from mpest.optimizers import ScipyTNC
from mpest.em.breakpointers import StepCountBreakpointer
from mpest.em.distribution_checkers import FiniteChecker
from mpest.em import EM

x = np.concatenate(
    (
        WeibullModelExp().generate(np.array([0.5, 1.0]), 100),
        GaussianModel().generate(np.array([5.0, 1.0]), 200),
    )
)
np.random.shuffle(x)

base_mixture_distribution = MixtureDistribution.from_distributions(
    [
        Distribution.from_params(WeibullModelExp, [0.5, 1.0]),
        Distribution.from_params(GaussianModel, [5.0, 1.0]),
    ]
)

problem = Problem(
    x,
    MixtureDistribution.from_distributions(
        [
            Distribution.from_params(WeibullModelExp, [1.0, 2.0]),
            Distribution.from_params(GaussianModel, [0.0, 5.0]),
        ]
    ),
)

em = EM(StepCountBreakpointer(max_step=8), FiniteChecker(), ScipyTNC())

result = em.solve(problem)


fig, axs = plt.subplots()
axs.set_xlabel("x")

sns.histplot(x, color="lightsteelblue")

axs_ = axs.twinx()
axs_.set_ylabel("p(x)")
axs_.set_yscale("log")

X = np.linspace(0.001, max(x), 2048)
axs_.plot(X, [base_mixture_distribution.pdf(x) for x in X], color="green", label="base")
axs_.plot(X, [result.content.pdf(x) for x in X], color="red", label="result")

plt.legend()
plt.show()
```
![plot](https://github.com/toxakaz/EM-algo/raw/main/examples/readme_example/example.png)

## Requirements
- python 3.11
- numpy
- scipy
