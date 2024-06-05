# Description
Initializes the model `EARM 1.3` by copying the base model `EARM 1.0`, adds a novel irreversible reaction for degrading DISC and shows how to rename existing components.

# Code
```
from __future__ import print_function
import re
from pysb import *
import pysb.bng

Start from EARM 1.0 as a base
==========
'http://identifiers.org/doi/10.1371/journal.pcbi.1002482',
          'isDescribedBy')
Rename all instances of Bcl2c to Mcl1, which was determined as a more accurate
description of that monomer based on its role in the model
==========
monomer
initial condition parameter
rule
Add one novel reaction
==========
degrade DISC
0.001)
DISC(b=None) >> L(b=None) + pR(b=None), kf31)
NOTE: In the original model this is a reversible reaction with kr31 as its
reverse rate constant, but kr31 was set to 0. This was ostensibly done so all
reactions had the same symmetric form, but I see no reason not to make it

```
