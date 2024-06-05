# Description
Check for equivalence between initial conditions and species when using compartments in the `pysb` library.

# Code
```

@with_model
def test_compartment_species_equivalence():
    Parameter('p', 1)
    Monomer('Q', ['x'])
    Monomer('R', ['y'])
    Compartment('C', None, 3, p)
    Rule('bind', Q(x=None) + R(y=None) >> Q(x=1) % R(y=1), p)
    Initial(Q(x=None) ** C, p)
    Initial(R(y=None) ** C, p)
    generate_equations(model)
    for i, ic in enumerate(model.initials):
        ok_(ic.pattern.is_equivalent_to(model.species[i]))

```
