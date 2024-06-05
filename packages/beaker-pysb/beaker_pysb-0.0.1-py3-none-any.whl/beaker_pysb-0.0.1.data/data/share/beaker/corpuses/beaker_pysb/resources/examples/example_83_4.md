# Description
Run a stochastic simulation on the EARM 1.0 model with multiple initial conditions for a species.

# Code
```
from pysb.simulator import StochKitSimulator
from pysb.examples import earm_1_0
from pysb.core import as_complex_pattern
import numpy as np

def test_stochkit_earm_multi_initials():
    model = earm_1_0.model
    tspan = np.linspace(0, 1000, 10)
    sim = StochKitSimulator(model, tspan=tspan)
    unbound_L = model.monomers['L'](b=None)
    simres = sim.run(initials={unbound_L: [3000, 1500]},
                     n_runs=2, seed=_STOCHKIT_SEED, algorithm="ssa")
    df = simres.dataframe

    unbound_L_index = model.get_species_index(as_complex_pattern(unbound_L))

    # Check we have two repeats of each initial
    assert np.allclose(df.loc[(slice(None), 0), '__s%d' % unbound_L_index],

```
