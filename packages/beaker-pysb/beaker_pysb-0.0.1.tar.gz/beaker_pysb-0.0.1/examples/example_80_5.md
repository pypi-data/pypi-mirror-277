# Description
Example of configuring and running the CupSodaSimulator with a specified number of blocks.

# Code
```
import numpy as np
from pysb.examples.tyson_oscillator import model

def test_n_blocks(self):
    print(self.solver.n_blocks)
    self.solver.n_blocks = 128
    assert self.solver.n_blocks == 128

```
