# Description
Accessing observable and expression concentrations at specific time points using pandas DataFrame.

# Code
```
from pysb.examples.expression_observables import model
from pysb.simulator import ScipyOdeSimulator
import numpy as np
np.set_printoptions(precision=4)
sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10), integrator_options={'atol': 1e-20})

>>> df = simulation_result.dataframe
>>> print(df.loc[5:15, ['Bax_c0', 'NBD_signal']]) \
    #doctest: +NORMALIZE_WHITESPACE
             Bax_c0  NBD_signal
time
8.888889   0.000138    4.995633

```
