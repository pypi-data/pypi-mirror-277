# Description
Define model annotations and initial parameters for the extrinsic apoptosis reaction model using PySB.

# Code
```
from __future__ import print_function
from pysb import *

Model()
Annotation(model, 'http://identifiers.org/biomodels.db/BIOMD0000000220', 'is')

transloc = .01; # rate of translocation between the cytosolic and mitochondrial compartments

v = .07; # mitochondria compartment volume/cell volume

# Non-zero initial conditions (in molecules per cell):
Parameter('L_0'        , 3000); # baseline level of ligand for most experiments (corresponding to 50 ng/ml SuperKiller TRAIL)
Parameter('pR_0'       , 200);  # TRAIL receptor (for experiments not involving siRNA)
Parameter('flip_0'     , 1e2);  # Flip
Parameter('pC8_0'      , 2e4);  # procaspase-8 (pro-C8)
Parameter('BAR_0'      , 1e3);  # Bifunctional apoptosis regulator
Parameter('pC3_0'      , 1e4);  # procaspase-3 (pro-C3)
Parameter('pC6_0'      , 1e4);  # procaspase-6 (pro-C6)  
Parameter('XIAP_0'     , 1e5);  # X-linked inhibitor of apoptosis protein  
Parameter('PARP_0'     , 1e6);  # C3* substrate
Parameter('Bid_0'      , 4e4);  # Bid
Parameter('Bcl2c_0'    , 2e4);  # cytosolic Bcl-2
Parameter('Bax_0'      , 1e5);  # Bax
Parameter('Bcl2_0'     , 2e4);  # mitochondrial Bcl-2  
Parameter('Mito_0'     , 5e5);  # mitochondrial binding sites for activated Bax
Parameter('mCytoC_0'   , 5e5);  # cytochrome c
Parameter('mSmac_0'    , 1e5);  # Smac    
Parameter('pC9_0'      , 1e5);  # procaspase-9 (pro-C9)

```
