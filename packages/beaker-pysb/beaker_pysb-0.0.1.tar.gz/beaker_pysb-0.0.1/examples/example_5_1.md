# Description
Simulate a model and display the results for an observable

# Code
```
import numpy
from pysb.simulator import ScipyOdeSimulator
from pysb.examples.robertson import model
from numpy import linspace

# Set print options for numpy arrays to improve readability
numpy.set_printoptions(precision=4)

# Define the function 'odesolve' if not available

>>> from pysb.examples.robertson import model
>>> from numpy import linspace
>>> numpy.set_printoptions(precision=4)
>>> yfull = odesolve(model, linspace(0, 40, 10))
>>> print(yfull['A_total'])            #doctest: +NORMALIZE_WHITESPACE
[1.      0.899   0.8506  0.8179  0.793   0.7728  0.7557  0.7408  0.7277

```
