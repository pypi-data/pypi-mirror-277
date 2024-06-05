# Description
Test SimulationResult.dataframe()

# Code
```
from pysb.simulator import ScipyOdeSimulator
import numpy as np

def test_simres_dataframe():
    """ Test SimulationResult.dataframe() """

    tspan1 = np.linspace(0, 100, 100)
    tspan2 = np.linspace(50, 100, 50)
    tspan3 = np.linspace(100, 150, 100)
    model = tyson_oscillator.model
    sim = ScipyOdeSimulator(model, integrator='lsoda')
    simres1 = sim.run(tspan=tspan1)
    # Check retrieving a single simulation dataframe
    df_single = simres1.dataframe

    # Generate multiple trajectories
    trajectories1 = simres1.species
    trajectories2 = sim.run(tspan=tspan2).species
    trajectories3 = sim.run(tspan=tspan3).species

    # Try a simulation result with two different tspan lengths
    sim = ScipyOdeSimulator(model, param_values={'k6' : [1.,1.]}, integrator='lsoda')
    simres = SimulationResult(sim, [tspan1, tspan2], [trajectories1, trajectories2])
    df = simres.dataframe

    assert df.shape == (len(tspan1) + len(tspan2),
                        len(model.species) + len(model.observables))

    # Next try a simulation result with two identical tspan lengths, stacked
    # into a single 3D array of trajectories
    simres2 = SimulationResult(sim, [tspan1, tspan3],
                               np.stack([trajectories1, trajectories3]))
    df2 = simres2.dataframe

    assert df2.shape == (len(tspan1) + len(tspan3),

```
