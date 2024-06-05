# Description
Generate a table of reversible binding reactions when either the row or column species (or both) have a complex bound to them using bind_table_complex function.

# Code
```

    Examples
    --------
    Binding table for two species types (R and C, which can be complexes or monomers)::

        Model()
        Monomer('R1', ['x', 'c1'])
        Monomer('R2', ['x', 'c1'])
        Monomer('C1', ['y', 'c2'])
        Monomer('C2', ['y', 'c2'])
        bind(C1(y=None), 'c2', C1(y=None), 'c2', (1e-3, 1e-2))
        bind(R1(x=None), 'c1', R2(x=None), 'c1', (1e-3, 1e-2))
        bind_table_complex([[              C1(c2=1, y=None)%C1(c2=1),            C2],
                           [R1()%R2(),  (1e-4, 1e-1),  (2e-4, 2e-1)],
                           [R2,     (3e-4, 3e-1),         None]],
                           'x', 'y', m1=R1(), m2=C1(y=None, c2=1))

    Execution:: 

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('R1', ['x', 'c1'])
        Monomer('R1', ['x', 'c1'])
        >>> Monomer('R2', ['x', 'c1'])
        Monomer('R2', ['x', 'c1'])
        >>> Monomer('C1', ['y', 'c2'])
        Monomer('C1', ['y', 'c2'])
        >>> Monomer('C2', ['y', 'c2'])
        Monomer('C2', ['y', 'c2'])
        >>> bind(C1(y=None), 'c2', C1(y=None), 'c2', (1e-3, 1e-2)) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('bind_C1_C1', C1(y=None, c2=None) + C1(y=None, c2=None) | C1(y=None, c2=1) % C1(y=None, c2=1), bind_C1_C1_kf, bind_C1_C1_kr),
         Parameter('bind_C1_C1_kf', 0.001),
         Parameter('bind_C1_C1_kr', 0.01),
         ])
        >>> bind(R1(x=None), 'c1', R2(x=None), 'c1', (1e-3, 1e-2)) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('bind_R1_R2', R1(x=None, c1=None) + R2(x=None, c1=None) | R1(x=None, c1=1) % R2(x=None, c1=1), bind_R1_R2_kf, bind_R1_R2_kr),
         Parameter('bind_R1_R2_kf', 0.001),
         Parameter('bind_R1_R2_kr', 0.01),
         ])
        >>> bind_table_complex([[               C1(c2=1, y=None)%C1(c2=1),           C2],
        ...                      [R1()%R2(),      (1e-4, 1e-1),                        (2e-4, 2e-1)],
        ...                       [R2,             (3e-4, 3e-1),                        None]],
        ...                       'x', 'y', m1=R1(), m2=C1(y=None, c2=1)) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
        Rule('bind_R1R2_C1C1', R1(x=None) % R2() + C1(y=None, c2=1) % C1(c2=1) | R1(x=50) % R2() % C1(y=50, c2=1) % C1(c2=1), bind_R1R2_C1C1_kf, bind_R1R2_C1C1_kr),
        Parameter('bind_R1R2_C1C1_kf', 0.0001),
        Parameter('bind_R1R2_C1C1_kr', 0.1),
        Rule('bind_R1R2_C2', R1(x=None) % R2() + C2(y=None) | R1(x=50) % R2() % C2(y=50), bind_R1R2_C2_kf, bind_R1R2_C2_kr),
        Parameter('bind_R1R2_C2_kf', 0.0002),
        Parameter('bind_R1R2_C2_kr', 0.2),
        Rule('bind_C1C1_R2', C1(y=None, c2=1) % C1(c2=1) + R2(x=None) | C1(y=50, c2=1) % C1(c2=1) % R2(x=50), bind_C1C1_R2_kf, bind_C1C1_R2_kr),
        Parameter('bind_C1C1_R2_kf', 0.0003),
        Parameter('bind_C1C1_R2_kr', 0.3),

```
