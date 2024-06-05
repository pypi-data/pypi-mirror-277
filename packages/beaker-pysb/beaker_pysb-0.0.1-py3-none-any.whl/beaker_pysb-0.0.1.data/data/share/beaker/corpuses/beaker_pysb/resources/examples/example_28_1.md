# Description
This example demonstrates how to define a simple three-species chemical kinetics system using PySB and generate the corresponding system of differential equations.

# Code
```
from __future__ import print_function

Model()

Monomer('A')
Monomer('B')
Monomer('C')

#       A -> B         0.04
Rule('A_to_B', A() >> B(), Parameter('k1', 0.04))
#      2B -> B + C     3.0e7
Rule('BB_to_BC', B() + B() >> B() + C(), Parameter('k2', 3.0e7))
#   B + C -> A + C     1.0e4
Rule('BC_to_AC', B() + C() >> A() + C(), Parameter('k3', 1.0e4))

# The system is known to be stiff for initial values A=1, B=0, C=0
Initial(A(), Parameter('A_0', 1.0))
Initial(B(), Parameter('B_0', 0.0))
Initial(C(), Parameter('C_0', 0.0))

# Observe total amount of each monomer
Observable('A_total', A())
Observable('B_total', B())

```
