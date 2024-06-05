# Description
Accessing species trajectories as a numpy ndarray from the SimulationResult object.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np
np.set_printoptions(precision=4)
sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), integrator_options={'atol': 1e-20})

>>> print(simulation_result.species) #doctest: +NORMALIZE_WHITESPACE
[[1.0000e+00   0.0000e+00   0.0000e+00]
 [1.1744e-02   5.2194e-02   9.3606e-01]
 [1.3791e-04   1.2259e-03   9.9864e-01]
 [1.6196e-06   2.1595e-05   9.9998e-01]
 [1.9020e-08   3.3814e-07   1.0000e+00]
 [2.2337e-10   4.9637e-09   1.0000e+00]
 [2.6232e-12   6.9951e-11   1.0000e+00]
 [3.0806e-14   9.5840e-13   1.0000e+00]
 [3.6178e-16   1.2863e-14   1.0000e+00]

```
