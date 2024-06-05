# Description
Defines the initial conditions for the model by setting parameter values corresponding to the initial amounts of different molecules (in molecules per cell) and creating monomers for each component of the model.

# Code
```
from pysb import *

# Non-zero initial conditions (in molecules per cell):
Parameter('L_0'        , 1500e3); # baseline level of ligand for most experiments (corresponding to 50 ng/ml SuperKiller TRAIL)
Parameter('pR_0'       , 170.999e3);  # TRAIL receptor (for experiments not involving siRNA)
Parameter('FADD_0'     , 133.165e3);
Parameter('flipL_0'    , 0.49995e3);  # FlipL 1X = 0.49995e3
Parameter('flipS_0'    , 0.422e3);  # Flip
Parameter('pC8_0'      , 200.168e3);  # procaspase-8 (pro-C8)
Parameter('Bid_0'       , 100e3);  # Bid

Monomer('L', ['b'])
Monomer('pR', ['b', 'rf'])
Monomer('FADD', ['rf', 'fe'])
Monomer('flipL', ['b', 'fe', 'ee', 'D384'],
        {'D384': ['U','C']}
        )
Monomer('flipS', ['b', 'fe', 'ee'])
Monomer('pC8', ['fe', 'ee', 'D384', 'D400'],
        {'D384': ['U','C'],
	 'D400': ['U','C']}
        )
Monomer('Bid') #called Apoptosis substrat in Lavrik's model

```
