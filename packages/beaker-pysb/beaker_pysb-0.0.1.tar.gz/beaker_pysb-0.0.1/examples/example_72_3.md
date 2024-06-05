# Description
Ensure the EARM 1.0 model simulates over a given time range.

# Code
```
from pysb.testing import *
from pysb.integrate import Solver
import numpy as np

def test_earm_integration():
    """Ensure earm_1_0 model simulates."""
    t = np.linspace(0, 1e3)
    # Run with or without inline
    sol = Solver(earm_1_0.model, t)
    sol.run()
    if Solver._use_inline:
        # Also run without inline
        Solver._use_inline = False
        sol = Solver(earm_1_0.model, t)
        sol.run()

```
