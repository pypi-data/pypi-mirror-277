# Description
Calculating observable trajectories on demand using the SimulationResult object.

# Code
```
from pysb import ANY
from pysb.examples import earm_1_0
from pysb.simulator import ScipyOdeSimulator
simres = ScipyOdeSimulator(earm_1_0.model, tspan=range(5)).run()

>>> simres.observable(m.Bid(b=ANY))
time
0    0.000000e+00
1    1.190933e-12
2    2.768582e-11
3    1.609716e-10
4    5.320530e-10

```
