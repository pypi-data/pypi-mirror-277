# Description
Run a Kappa simulation with multiple initial conditions to check proper handling of variable initial conditions.

# Code
```
pysb.simulator import KappaSimulator
pysb.examples import michment

def test_kappa_2initials():
    sim = KappaSimulator(michment.model, tspan=np.linspace(0, 100, 101))
    res = sim.run(initials={
        michment.model.initials[0].pattern: [10, 100],
        michment.model.initials[1].pattern: [100, 1000]
    }, seed=KAPPA_SEED)

```
