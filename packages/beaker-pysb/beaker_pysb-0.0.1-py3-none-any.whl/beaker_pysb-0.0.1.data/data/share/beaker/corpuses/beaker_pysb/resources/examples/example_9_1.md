# Description
Demonstrates how to use the get_half_bonds_in_pattern function to extract bond numbers used in a pattern.

# Code
```
from pysb import Monomer

A = Monomer('A', ['b1', 'b2'], _export=False)
get_half_bonds_in_pattern(A(b1=None, b2=None))
get_half_bonds_in_pattern(A(b1=1) % A(b2=1))

```
