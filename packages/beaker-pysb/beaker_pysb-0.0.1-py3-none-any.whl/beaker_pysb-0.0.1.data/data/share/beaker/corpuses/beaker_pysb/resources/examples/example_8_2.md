# Description
Generate the reversible binding reaction S1 + S2 | S1:S2 using bind function.

# Code
```

    Examples
    --------
    Binding between A and B::

        Model()
        Monomer('A', ['x'])
        Monomer('B', ['y'])
        bind(A, 'x', B, 'y', [1e-4, 1e-1])

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A', ['x'])
        Monomer('A', ['x'])
        >>> Monomer('B', ['y'])
        Monomer('B', ['y'])
        >>> bind(A, 'x', B, 'y', [1e-4, 1e-1]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('bind_A_B', A(x=None) + B(y=None) | A(x=1) % B(y=1), bind_A_B_kf, bind_A_B_kr),
         Parameter('bind_A_B_kf', 0.0001),
         Parameter('bind_A_B_kr', 0.1),

```
