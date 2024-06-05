# Description
Run a Kappa simulation with two runs to verify the simulation count.

# Code
```
pysb.simulator import KappaSimulator
pysb.examples import michment

def test_kappa_2sims():
    sim = KappaSimulator(michment.model, tspan=np.linspace(0, 100, 101))
    res = sim.run(n_runs=2, seed=KAPPA_SEED)

```
