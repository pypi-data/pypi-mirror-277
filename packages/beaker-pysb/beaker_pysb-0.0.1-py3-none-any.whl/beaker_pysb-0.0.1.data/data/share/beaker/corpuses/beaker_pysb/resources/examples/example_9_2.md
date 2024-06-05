# Description
Demonstrates how to use the get_bonds_in_pattern function to extract a set of bond numbers used in a pattern.

# Code
```
from pysb import Monomer

A = Monomer('A', ['b1', 'b2'], _export=False)
get_bonds_in_pattern(A(b1=None, b2=None)) == set()
get_bonds_in_pattern(A(b1=1) % A(b2=1)) == {1}
get_bonds_in_pattern(A(b1=1) % A(b1=2, b2=1) % A(b1=2)) == {1, 2}

```
