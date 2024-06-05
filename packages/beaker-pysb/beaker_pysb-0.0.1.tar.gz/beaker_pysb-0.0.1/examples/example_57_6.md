# Description
Accessing combined array of species, observables, and expressions.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np
np.set_printoptions(precision=4)
sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), integrator_options={'atol': 1e-20})

    >>> print(simulation_result.all[0]) #doctest: +SKIP

```
