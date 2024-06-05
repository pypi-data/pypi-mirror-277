# Description
Generate the reversible binding reaction S1 + S2 | S1:S2 with optional complexes attached using bind_complex function.

# Code
```

    Examples
    --------

    Binding between ``A:B`` and ``C:D``:

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A', ['a', 'b'])
        Monomer('A', ['a', 'b'])
        >>> Monomer('B', ['c', 'd'])
        Monomer('B', ['c', 'd'])
        >>> Monomer('C', ['e', 'f'])
        Monomer('C', ['e', 'f'])
        >>> Monomer('D', ['g', 'h'])
        Monomer('D', ['g', 'h'])
        >>> bind_complex(A(a=1) % B(c=1), 'b', C(e=2) % D(g=2), 'h', [1e-4, \
            1e-1]) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
        Rule('bind_AB_DC', A(a=1, b=None) % B(c=1) + D(g=3, h=None) % C(e=3)
          | A(a=1, b=50) % B(c=1) % D(g=3, h=50) % C(e=3), bind_AB_DC_kf,
          bind_AB_DC_kr),
        Parameter('bind_AB_DC_kf', 0.0001),
        Parameter('bind_AB_DC_kr', 0.1),
        ])

    Execution:

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A', ['a', 'b'])
        Monomer('A', ['a', 'b'])
        >>> Monomer('B', ['c', 'd'])
        Monomer('B', ['c', 'd'])
        >>> Monomer('C', ['e', 'f'])
        Monomer('C', ['e', 'f'])
        >>> Monomer('D', ['g', 'h'])
        Monomer('D', ['g', 'h'])
        >>> bind(A, 'a', B, 'c', [1e4, 1e-1]) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
        Rule('bind_A_B',
          A(a=None) + B(c=None) | A(a=1) % B(c=1),
          bind_A_B_kf, bind_A_B_kr),
        Parameter('bind_A_B_kf', 10000.0),
        Parameter('bind_A_B_kr', 0.1),
        ])
        >>> bind(C, 'e', D, 'g', [1e4, 1e-1]) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
        Rule('bind_C_D',
          C(e=None) + D(g=None) | C(e=1) % D(g=1),
          bind_C_D_kf, bind_C_D_kr),
        Parameter('bind_C_D_kf', 10000.0),
        Parameter('bind_C_D_kr', 0.1),
        ])
        >>> bind_complex(A(a=1) % B(c=1), 'b', C(e=2) % D(g=2), 'h', [1e-4, \
            1e-1]) #doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
        Rule('bind_AB_DC',
          A(a=1, b=None) % B(c=1) + D(g=3, h=None) % C(e=3) | A(a=1,
          b=50) % B(c=1) % D(g=3, h=50) % C(e=3),
          bind_AB_DC_kf, bind_AB_DC_kr),
        Parameter('bind_AB_DC_kf', 0.0001),
        Parameter('bind_AB_DC_kr', 0.1),

```
