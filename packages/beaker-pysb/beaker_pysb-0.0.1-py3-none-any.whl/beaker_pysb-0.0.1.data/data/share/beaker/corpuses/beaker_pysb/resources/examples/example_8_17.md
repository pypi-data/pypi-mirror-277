# Description
Generate rules to assemble a homomeric chain sequentially using assemble_chain_sequential function.

# Code
```

    Assemble a three-membered chain by sequential addition of monomers,
    with the same forward/reverse rates for monomer-monomer and monomer-dimer
    interactions::

        Model()
        Monomer('Unit', ['p1', 'p2'])
        assemble_chain_sequential(Unit, 'p1', 'p2', 3, [[1e-4, 1e-1]] * 2)

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('Unit', ['p1', 'p2'])
        Monomer('Unit', ['p1', 'p2'])
        >>> assemble_chain_sequential(Unit, 'p1', 'p2', 3, [[1e-4, 1e-1]] * 2) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('assemble_chain_sequential_Unit_2', Unit(p1=None, p2=None) + Unit(p1=None, p2=None) | Unit(p1=None, p2=1) % Unit(p1=1, p2=None), assemble_chain_sequential_Unit_2_kf, assemble_chain_sequential_Unit_2_kr),
         Parameter('assemble_chain_sequential_Unit_2_kf', 0.0001),
         Parameter('assemble_chain_sequential_Unit_2_kr', 0.1),
         Rule('assemble_chain_sequential_Unit_3', Unit(p1=None, p2=None) + Unit(p1=None, p2=1) % Unit(p1=1, p2=None) | MatchOnce(Unit(p1=None, p2=1) % Unit(p1=1, p2=2) % Unit(p1=2, p2=None)), assemble_chain_sequential_Unit_3_kf, assemble_chain_sequential_Unit_3_kr),
         Parameter('assemble_chain_sequential_Unit_3_kf', 0.0001),
         Parameter('assemble_chain_sequential_Unit_3_kr', 0.1),

```
