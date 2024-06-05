# Description
This example shows how to generate the system of differential equations from the defined model in PySB, making the equations resemble the original mathematical representation by substituting PySB's internal symbols.

# Code
```
from __future__ import print_function
from pysb import *
Model()
Monomer('A')
Monomer('B')
Monomer('C')
Rule('A_to_B', A() >> B(), Parameter('k1', 0.04))
Rule('BB_to_BC', B() + B() >> B() + C(), Parameter('k2', 3.0e7))
Rule('BC_to_AC', B() + C() >> A() + C(), Parameter('k3', 1.0e4))
Initial(A(), Parameter('A_0', 1.0))
Initial(B(), Parameter('B_0', 0.0))
Initial(C(), Parameter('C_0', 0.0))
Observable('A_total', A())
Observable('B_total', B())

if __name__ == '__main__':
    from pysb.bng import generate_equations

    # This creates model.odes which contains the math
    generate_equations(model)

    # Build a symbol substitution mapping to help the math look like the
    # equations in the comment above, instead of showing the internal pysb
    # symbol names
    # ==========
    substitutions = {}
    # Map parameter symbols to their values
    substitutions.update((p.name, p.value) for p in model.parameters)
    # Map species variables sI to yI+1, e.g. s0 -> y1
    substitutions.update(('s%d' % i, 'y%d' % (i+1))
                         for i in range(len(model.odes)))

    print(__doc__, "\n", model, "\n")

    # Iterate over each equation
    for i, eq in enumerate(model.odes):
        # Perform the substitution using the sympy 'subs' method and the
        # mappings we built above
        eq_sub = eq.subs(substitutions)
        # Display the equation
        print('y%d\' = %s' % (i+1, eq_sub))

    print("""
NOTE: This model code is designed to be imported and programatically
manipulated, not executed directly. The above output is merely a

```
