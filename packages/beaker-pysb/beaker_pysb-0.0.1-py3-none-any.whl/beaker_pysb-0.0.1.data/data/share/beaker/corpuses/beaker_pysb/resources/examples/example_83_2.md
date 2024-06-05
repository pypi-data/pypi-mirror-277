# Description
Run a stochastic simulation with an invalid keyword argument, expecting it to raise a ValueError.

# Code
```
pysb.simulator import StochKitSimulator
pysb.examples import earm_1_0

@raises(ValueError)
def test_stochkit_invalid_init_kwarg():

```
