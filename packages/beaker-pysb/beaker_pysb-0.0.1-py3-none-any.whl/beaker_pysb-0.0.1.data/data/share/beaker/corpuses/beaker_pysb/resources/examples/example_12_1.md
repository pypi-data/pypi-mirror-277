# Description
Generate synthetic data using a model and perturb it by adding noise.

# Code
```
import numpy
from pysb import ComponentSet

def synthetic_data(model, tspan, obs_list=None, sigma=0.1):
    #from pysb.integrate import odesolve
    from pysb.integrate import Solver
    solver = Solver(model, tspan)
    solver.run()

    # Sample from a normal distribution with variance sigma and mean 1
    # (randn generates a matrix of random numbers sampled from a normal
    # distribution with mean 0 and variance 1)
    # 
    # Note: This modifies yobs_view (the view on yobs) so that the changes 
    # are reflected in yobs (which is returned by the function). Since a new
    # Solver object is constructed for each function invocation this does not
    # cause problems in this case.
    solver.yobs_view *= ((numpy.random.randn(*solver.yobs_view.shape) * sigma) + 1)

```
