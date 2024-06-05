# Description
Simulate a model using network free simulation (NFsim)

# Code
```
import numpy as np
from pysb.examples import robertson

from pysb.examples import robertson
from pysb.simulator.bng import BngSimulator
model = robertson.model
sim = BngSimulator(model, tspan=np.linspace(0, 1))

```
