# Description
Example to ensure the 'robertson' model simulates correctly

# Code
```
from pysb.simulator import ScipyOdeSimulator, CythonRhsBuilder
import numpy as np

def test_robertson_integration():
    """Ensure robertson model simulates."""
    t = np.linspace(0, 100)
    sim = ScipyOdeSimulator(robertson.model, tspan=t, compiler="python")
    simres = sim.run()
    assert simres.species.shape[0] == t.shape[0]
    # Also run with cython compiler if available.
    if CythonRhsBuilder.check_safe():
        sim = ScipyOdeSimulator(robertson.model, tspan=t, compiler="cython")
        simres = sim.run()

```
