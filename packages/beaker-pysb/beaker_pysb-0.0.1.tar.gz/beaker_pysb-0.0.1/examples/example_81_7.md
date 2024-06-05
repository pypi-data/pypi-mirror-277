# Description
Use the model equations generation with a Kappa simulation for a single time point to ensure proper handling and output verification.

# Code
```
pysb.simulator import KappaSimulator
pysb.bng import generate_equations
pysb.examples import michment

def test_kappa_1timepoint_with_netgen():
    generate_equations(michment.model)
    sim = KappaSimulator(michment.model, tspan=[0, 1])
    # This set of parameter values causes Kappa to abort after 1st time point
    res = sim.run(param_values=[100, 100, 10, 10, 100, 100], seed=KAPPA_SEED)

```
