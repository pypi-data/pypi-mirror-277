# Description
Ensure a warning is raised when a nonexistent integrator is specified.

# Code
```
from pysb.testing import raises
from pysb.integrate import Solver
import numpy as np

@raises(UserWarning)
def test_nonexistent_integrator():
    """Ensure nonexistent integrator raises."""

```
