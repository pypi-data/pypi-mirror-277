# Description
Generate a table of reversible binding reactions between R and C using bind_table function.

# Code
```

    Examples
    --------
    Binding table for two species types (R and C), each with two members::

        Model()
        Monomer('R1', ['x'])
        Monomer('R2', ['x'])
        Monomer('C1', ['y'])
        Monomer('C2', ['y'])
        bind_table([[               C1,           C2],
                    [R1,  (1e-4, 1e-1),  (2e-4, 2e-1)],
                    [R2,  (3e-4, 3e-1),         None]],
                   'x', 'y')

    Execution:: 

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('R1', ['x'])
        Monomer('R1', ['x'])
        >>> Monomer('R2', ['x'])
        Monomer('R2', ['x'])
        >>> Monomer('C1', ['y'])
        Monomer('C1', ['y'])
        >>> Monomer('C2', ['y'])
        Monomer('C2', ['y'])
        >>> bind_table([[               C1,           C2],
        ...             [R1,  (1e-4, 1e-1),  (2e-4, 2e-1)],
        ...             [R2,  (3e-4, 3e-1),         None]],
        ...            'x', 'y') # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('bind_R1_C1', R1(x=None) + C1(y=None) | R1(x=1) % C1(y=1),
             bind_R1_C1_kf, bind_R1_C1_kr),
         Parameter('bind_R1_C1_kf', 0.0001),
         Parameter('bind_R1_C1_kr', 0.1),
         Rule('bind_R1_C2', R1(x=None) + C2(y=None) | R1(x=1) % C2(y=1),
             bind_R1_C2_kf, bind_R1_C2_kr),
         Parameter('bind_R1_C2_kf', 0.0002),
         Parameter('bind_R1_C2_kr', 0.2),
         Rule('bind_R2_C1', R2(x=None) + C1(y=None) | R2(x=1) % C1(y=1),
             bind_R2_C1_kf, bind_R2_C1_kr),
         Parameter('bind_R2_C1_kf', 0.0003),
         Parameter('bind_R2_C1_kr', 0.3),

```
