# Description
Setup and run SSA simulations using CUDA SSASimulator for multiple parameters.

# Code
```
import numpy as np
from pysb.examples.schloegl import model
from pysb.simulator import CudaSSASimulator
model.parameters['X_0'].value = 400
simulator = CudaSSASimulator(model)
tspan = np.linspace(0, 100, 101)

def test_run_by_multi_params(self):
    param_values = np.array(
        [p.value for p in self.model.parameters])
    param_values = np.repeat([param_values], self.n_sim, axis=0)

```
