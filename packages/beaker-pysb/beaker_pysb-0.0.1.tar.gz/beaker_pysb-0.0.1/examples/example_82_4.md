# Description
Example to ensure the 'earm_1_0' model simulates correctly

# Code
```
pysb.examples import earm_1_0
pysb.simulator import ScipyOdeSimulator, CythonRhsBuilder

def test_earm_integration():
    """Ensure earm_1_0 model simulates."""
    t = np.linspace(0, 1e3)
    sim = ScipyOdeSimulator(earm_1_0.model, tspan=t, compiler="python")
    sim.run()
    # Also run with cython compiler if available.
    if CythonRhsBuilder.check_safe():

```
