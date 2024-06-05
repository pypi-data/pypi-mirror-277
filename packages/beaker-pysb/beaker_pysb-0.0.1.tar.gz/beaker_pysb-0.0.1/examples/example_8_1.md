# Description
Generate the unimolecular reversible equilibrium reaction S1 <-> S2 using equilibrate function.

# Code
```

    --------
    Simple two-state equilibrium between A and B::

        Model()
        Monomer('A')
        Monomer('B')
        equilibrate(A(), B(), [1, 1])
    
    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A')
        Monomer('A')
        >>> Monomer('B')
        Monomer('B')
        >>> equilibrate(A(), B(), [1, 1]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('equilibrate_A_to_B', A() | B(), equilibrate_A_to_B_kf, equilibrate_A_to_B_kr),
         Parameter('equilibrate_A_to_B_kf', 1.0),
         Parameter('equilibrate_A_to_B_kr', 1.0),

```
