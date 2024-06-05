# Description
Accessing observables from the SimulationResult object.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np
np.set_printoptions(precision=4)
sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), integrator_options={'atol': 1e-20})

>>> print(simulation_result.observables['Bax_c0']) \
    #doctest: +NORMALIZE_WHITESPACE
[1.0000e+00   1.1744e-02   1.3791e-04   1.6196e-06   1.9020e-08

```
