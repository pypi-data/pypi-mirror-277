# Description
Run a Kappa simulation with custom parameter values and verify that results for different simulations are identical.

# Code
```
pysb.simulator import KappaSimulator
pysb.examples import michment

def test_kappa_2params():
    base_param_values = np.array(
        [p.value for p in michment.model.parameters] * 2
    ).reshape(2, len(michment.model.parameters))
    sim = KappaSimulator(michment.model, tspan=np.linspace(0, 100, 101))

    res = sim.run(param_values=base_param_values, seed=KAPPA_SEED)
    assert res.nsims == 2

```
