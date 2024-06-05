# Description
Another example of calculating an observable trajectory on demand using a different pattern.

# Code
```
from pysb import ANY
from pysb.examples import earm_1_0
from pysb.simulator import ScipyOdeSimulator
simres = ScipyOdeSimulator(earm_1_0.model, tspan=range(5)).run()

>>> simres.observable(m.AMito(b=1) % m.mCytoC(b=1))
time
0    0.000000e+00
1    1.477319e-77
2    1.669917e-71
3    5.076939e-69
4    1.157400e-66

```
