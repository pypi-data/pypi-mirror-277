# Description
Simulate a model and display the results for an observable using the StochKitSimulator from PySB.

# Code
```
pysb.simulator.base import Simulator, SimulationResult, SimulatorException
pysb.bng import generate_equations
pysb.export.stochkit import StochKitExporter
numpy as np
pysb.pathfinder import get_path
pysb.logging import EXTENDED_DEBUG

    >>> sim = StochKitSimulator(model, tspan=np.linspace(0, 10, 5))

    Here we supply a "seed" to the random number generator for deterministic
    results, but for most purposes it is recommended to leave this blank.

    >>> simulation_result = sim.run(n_runs=2, seed=123456)

    A_total trajectory for first run

    >>> print(simulation_result.observables[0]['A_total']) \
        #doctest: +NORMALIZE_WHITESPACE
    [1.  0.  0.  0.  0.]

    A_total trajectory for second run

    >>> print(simulation_result.observables[1]['A_total']) \

```
