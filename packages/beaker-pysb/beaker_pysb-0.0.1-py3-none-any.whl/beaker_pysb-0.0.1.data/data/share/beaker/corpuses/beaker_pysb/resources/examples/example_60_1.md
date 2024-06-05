# Description
Example of how to simulate a model using Kappa with the KappaSimulator class.

# Code
```
import numpy as np
from pysb.examples import michment

import numpy as np
from pysb.examples import michment
from pysb.simulator import KappaSimulator
sim = KappaSimulator(michment.model, tspan=np.linspace(0, 1))

```
