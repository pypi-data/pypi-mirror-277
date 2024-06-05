# Description
Obtain a view on a returned record array which uses an atomic data-type and integer indexing

# Code
```
import numpy
from pysb.simulator import ScipyOdeSimulator
from pysb.examples.robertson import model
from numpy import linspace

# Set print options for numpy arrays to improve readability
numpy.set_printoptions(precision=4)

# Define the function 'odesolve' if not available
# Here we assume that 'odesolve' has been defined as depicted in the provided code


>>> yfull.shape == (10, )
True
>>> print(yfull.dtype)                 #doctest: +NORMALIZE_WHITESPACE
[('__s0', '<f8'), ('__s1', '<f8'), ('__s2', '<f8'), ('A_total', '<f8'),
('B_total', '<f8'), ('C_total', '<f8')]
>>> print(yfull[0:4, 1:3])             #doctest: +ELLIPSIS
Traceback (most recent call last):
  ...
IndexError: too many indices...
>>> yarray = yfull.view(float).reshape(len(yfull), -1)
>>> yarray.shape == (10, 6)
True
>>> print(yarray.dtype)
float64
>>> print(yarray[0:4, 1:3])            #doctest: +NORMALIZE_WHITESPACE
[[0.0000e+00   0.0000e+00]
 [2.1672e-05   1.0093e-01]
 [1.6980e-05   1.4943e-01]

```
