# Description
A test to set initial conditions by changing their underlying parameter values and running a simulation with BngSimulator.

# Code
```
from pysb.testing import *
import numpy as np
from pysb.simulator.bng import BngSimulator
from pysb.examples import robertson


def test_set_initials_by_params():
    # This tests setting initials by changing their underlying parameter values
    # BNG Simulator uses a dictionary for initials, unlike e.g.
    # ScipyOdeSimulator, so a separate test is needed

    model = robertson.model
    t = np.linspace(0, 40, 51)
    ic_params = model.parameters_initial_conditions()
    param_values = np.array([p.value for p in model.parameters])
    ic_mask = np.array([p in ic_params for p in model.parameters])

    bng_sim = BngSimulator(model, tspan=t, verbose=0)

    # set all initial conditions to 1
    param_values[ic_mask] = np.array([1, 1, 1])
    traj = bng_sim.run(param_values=param_values)

    # set properly here
    assert np.allclose(traj.initials, [1, 1, 1])

    # overwritten in bng file. lines 196-202.
    # Values from initials_dict are used, but it should take them from
    # self.initials, so I don't see how they are getting overwritten?
    print(traj.dataframe.loc[0])
    assert np.allclose(traj.dataframe.loc[0][0:3], [1, 1, 1])

    # Same here
    param_values[ic_mask] = np.array([0, 1, 1])
    traj = bng_sim.run(param_values=param_values)
    assert np.allclose(traj.initials, [0, 1, 1])

```
