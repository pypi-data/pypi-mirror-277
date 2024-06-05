# Description
Run a Kappa simulation with a single time point, ensuring that Kappa correctly handles this case.

# Code
```
pysb.simulator import KappaSimulator
pysb.examples import michment

def test_kappa_1timepoint():
    michment.model.reset_equations()
    sim = KappaSimulator(michment.model, tspan=[0, 1])
    # This set of parameter values causes Kappa to abort after 1st time point
    res = sim.run(param_values=[100, 100, 10, 10, 100, 100], seed=KAPPA_SEED)

```
