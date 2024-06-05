# Description
Ensure the Robertson model simulates over a given time range.

# Code
```
from pysb.testing import *
from pysb.integrate import Solver
import numpy as np

def test_robertson_integration():
    """Ensure robertson model simulates."""
    t = np.linspace(0, 100)
    # Run with or without inline
    sol = Solver(robertson.model, t)
    sol.run()
    assert sol.y.shape[0] == t.shape[0]
    if Solver._use_inline:
        # Also run without inline
        Solver._use_inline = False
        sol = Solver(robertson.model, t)
        sol.run()
        assert sol.y.shape[0] == t.shape[0]

```
