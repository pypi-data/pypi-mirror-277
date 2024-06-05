# Description
Run a Kappa simulation on the Michment model, apply a perturbation, and compare the results with a reference simulation.

# Code
```
pysb.simulator import KappaSimulator
pysb.kappa import run_simulation
pysb.examples import michment

def test_kappa_sim_michment():
    perturbation = '%init: 12 E(s[.])'

    orig_sim = run_simulation(michment.model, time=100, points=100,
                              seed=KAPPA_SEED, perturbation=perturbation)

    sim = KappaSimulator(michment.model, tspan=np.linspace(0, 100, 101))
    x = sim.run(seed=KAPPA_SEED, perturbation=perturbation)


```
