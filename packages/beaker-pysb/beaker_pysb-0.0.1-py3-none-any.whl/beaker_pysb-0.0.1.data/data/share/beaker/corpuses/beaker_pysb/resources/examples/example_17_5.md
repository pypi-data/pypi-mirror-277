# Description
Generate initial conditions based on parameter naming conventions.

# Code
```
from pysb import *

Model()

# Example parameter definition
def ExampleModel():
    Parameter('Bid_0', 4e4)
    Parameter('PARP_0', 1e6)
    Parameter('mSmac_0', 1e5)
    Parameter('tBid_0', 1.0)
    Parameter('CPARP_0', 1.0)

# generate initial conditions from _0 parameter naming convention
for m in model.monomers:
    ic_param = model.parameters.get('%s_0' % m.name)
    if ic_param is not None:
        sites = {}
        for s in m.sites:
            if s in m.site_states:
                sites[s] = m.site_states[s][0]
            else:
                sites[s] = None

```
