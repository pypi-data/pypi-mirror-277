# Description
Perform sequential simulations with network reloading using the `pysb` library.

# Code
```
from pysb import *

@with_model
def test_sequential_simulations():
    Monomer('A')
    Parameter('A_0', 1)
    Initial(A(), A_0)
    Parameter('k', 1)
    Rule('degrade', A() >> None, k)
    # Suppress network overwrite warning from simulate command
    with BngFileInterface(model) as bng:
        bng.action('generate_network')
        bng.action('simulate', method='ssa', t_end=20000, n_steps=100)
        bng.execute()
        yfull1 = bng.read_simulation_results()
        ok_(yfull1.size == 101)

        # Run another simulation by reloading the existing network file
        bng.action('simulate', method='ssa', t_end=10000, n_steps=50)
        bng.execute(reload_netfile=True)
        yfull2 = bng.read_simulation_results()

```
