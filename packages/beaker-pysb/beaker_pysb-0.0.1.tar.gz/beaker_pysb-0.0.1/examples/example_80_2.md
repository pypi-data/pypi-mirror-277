# Description
Example of verifying the integrator options set in the CupSodaSimulator.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_integrator_options(self):
    assert self.solver.opts['atol'] == 1e-12
    assert self.solver.opts['rtol'] == 1e-12

```
