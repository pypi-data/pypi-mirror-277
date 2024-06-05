# Description
Example of running the CupSodaSimulator with different memory usage options.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_memory_usage(self):
    assert self.solver.opts['memory_usage'] == 'sharedconstant'
    self.solver.run(initials=self.y0)  # memory_usage='sharedconstant'
    self.solver.opts['memory_usage'] = 'global'
    self.solver.run(initials=self.y0)
    self.solver.opts['memory_usage'] = 'shared'

```
