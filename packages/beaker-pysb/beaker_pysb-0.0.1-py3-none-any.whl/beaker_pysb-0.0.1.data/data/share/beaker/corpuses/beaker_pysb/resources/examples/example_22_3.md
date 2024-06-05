# Description
Defines the observable species, which allows for tracking the amounts of these species during the simulation.

# Code
```
from pysb import *
Model()

Parameter('L_0', 1500e3)
Parameter('pR_0', 170.999e3)
Parameter('FADD_0', 133.165e3)
Parameter('flipL_0', 0.49995e3)
Parameter('flipS_0', 0.422e3)
Parameter('pC8_0', 200.168e3)
Parameter('Bid_0', 100e3)
Monomer('L', ['b'])
Monomer('pR', ['b', 'rf'])
Monomer('FADD', ['rf', 'fe'])
Monomer('flipL', ['b', 'fe', 'ee', 'D384'], {'D384': ['U', 'C']})
Monomer('flipS', ['b', 'fe', 'ee'])
Monomer('pC8', ['fe', 'ee', 'D384', 'D400'], {'D384': ['U', 'C'], 'D400': ['U', 'C']})
Monomer('Bid')
Monomer('tBid')
flip_monomers = (flipL, flipS)


Observable('p18', pC8(fe=None, ee=1, D384='C',D400='C') % pC8(fe=None, ee=1, D384='C',D400='C'))

```
