# Description
Example of setting up and running the CupSodaSimulator with specific initial concentrations and checking the volume attribute.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_use_of_volume(self):
    # Initial concentrations
    self.solver.run(initials=self.y0)
    print(self.solver.vol)
    assert self.solver.vol is None
    self.solver.vol = 1e-20

```
