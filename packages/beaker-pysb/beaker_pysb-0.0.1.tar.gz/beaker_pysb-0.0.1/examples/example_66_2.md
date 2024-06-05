# Description
Simulate a network using the BNG Console interface with the `pysb` library on non-Windows systems.

# Code
```
from pysb import *
from pysb.bng import *
import os

@unittest.skipIf(os.name == 'nt', 'BNG Console does not work on Windows')
@with_model
def test_simulate_network_console():
    Monomer('A')
    Parameter('A_0', 1)
    Initial(A(), A_0)
    Parameter('k', 1)
    Rule('degrade', A() >> None, k)
    with BngConsole(model) as bng:
        bng.generate_network()

```
