# Description
Retrieving the value of all observables at a particular time point from the SimulationResult object.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np
np.set_printoptions(precision=4)
sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), integrator_options={'atol': 1e-20})

>>> print(simulation_result.observables[-1]) \
    #doctest: +SKIP

```
