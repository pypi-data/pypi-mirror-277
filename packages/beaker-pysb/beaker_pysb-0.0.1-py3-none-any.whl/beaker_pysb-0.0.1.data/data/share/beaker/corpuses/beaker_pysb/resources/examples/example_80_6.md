# Description
Example of running multiple simulation chunks with the CupSodaSimulator.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_multi_chunks(self):
    sim = CupSodaSimulator(model, tspan=self.tspan, verbose=False,
                           initials=self.y0,
                           integrator_options={'atol': 1e-12,
                                               'rtol': 1e-12,
                                               'chunksize': 25,
                                               'max_steps': 20000})
    res = sim.run()

```
