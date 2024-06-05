# Description
Define observables for the model to monitor specific species during simulations.

# Code
```
from pysb import *

Model()

# Example declarations for monomers
Monomer('Bid', ['b'])
Monomer('PARP', ['b'])
Monomer('mSmac', ['b'])
Monomer('tBid', ['b'])
Monomer('CPARP', ['b'])

# Fig 4B
Observable('Bid_unbound',   Bid(b=None))
Observable('PARP_unbound',  PARP(b=None))
Observable('mSmac_unbound', mSmac(b=None))
# this is what I originally thought 4B was actually plotting -JLM
Observable('tBid_total',  tBid())
Observable('CPARP_total', CPARP())

```
