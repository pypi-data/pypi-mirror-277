# Description
Using ScipyOdeSimulator to run a simulation with a model.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np

>>> sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), \
                            integrator_options={'atol': 1e-20})

```
