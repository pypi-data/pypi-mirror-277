# Description
Example of setting up and running the CupSodaSimulator with specific parameters and verifying the results.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_run_tyson(self):
    # Rate constants
    len_parameters = len(model.parameters)
    param_values = np.ones((self.n_sims, len_parameters))
    for j in range(len_parameters):
        param_values[:, j] *= model.parameters[j].value
    simres = self.solver.run(initials=self.y0)
    print(simres.observables)
    self.solver.run(param_values=None, initials=self.y0)
    self.solver.run(param_values=param_values, initials=self.y0)

```
