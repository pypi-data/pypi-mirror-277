# Description
Example of testing the CupSodaSimulator for handling invalid integrator options.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model
from pysb.simulator.cupsoda import CupSodaSimulator

def test_invalid_integrator_option(self):
    CupSodaSimulator(model, tspan=self.tspan,

```
