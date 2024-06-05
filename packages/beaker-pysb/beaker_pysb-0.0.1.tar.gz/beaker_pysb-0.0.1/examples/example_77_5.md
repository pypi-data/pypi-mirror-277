# Description
Test saving and loading observables and expressions

# Code
```
import io
from pysb.simulator import ScipyOdeSimulator
from pysb.simulator.base import SimulationResult
import numpy as np
from pysb.examples import tyson_oscillator

def test_save_load_observables_expressions():
    buff = io.BytesIO()
    tspan = np.linspace(0, 100, 100)
    sim = ScipyOdeSimulator(tyson_oscillator.model, tspan).run()
    sim.save(buff, include_obs_exprs=True)

    sim2 = SimulationResult.load(buff)
    assert len(sim2.observables) == len(tspan)
    # Tyson oscillator doesn't have expressions

```
