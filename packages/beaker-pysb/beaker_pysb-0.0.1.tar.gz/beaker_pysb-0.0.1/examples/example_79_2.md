# Description
Setup and run SSA simulations using CUDA SSASimulator for multiple initial conditions specified as a dictionary.

# Code
```
import numpy as np
from pysb.examples.schloegl import model
from pysb.simulator import CudaSSASimulator
model.parameters['X_0'].value = 400
simulator = CudaSSASimulator(model)
tspan = np.linspace(0, 100, 101)

def test_run_by_multi_initials_df(self):
    initials = dict()
    n_sim = 10
    for ic in self.model.initial_conditions:
        initials[ic[0]] = [ic[1].value] * n_sim
    self.simulator.run(self.tspan, initials=initials)

```
