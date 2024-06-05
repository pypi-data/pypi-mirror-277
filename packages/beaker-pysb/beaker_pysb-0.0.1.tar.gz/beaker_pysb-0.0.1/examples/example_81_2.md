# Description
Run a Kappa simulation with an invalid argument to ensure it raises a ValueError.

# Code
```
pysb.simulator import KappaSimulator
pysb.examples import michment

@raises(ValueError)
def test_kappa_sim_invalid_arg():
    sim = KappaSimulator(michment.model, tspan=range(10))

```
