# Description
Example of initializing the CupSodaSimulator with verbose output and specific options.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_verbose(self):
    solver = CupSodaSimulator(model, tspan=self.tspan, verbose=True,
                              integrator_options={'atol': 1e-12,
                                                  'rtol': 1e-12,
                                                  'vol': 1e-5,
                                                  'max_steps': 20000})

```
