# Description
Generate a table of synthesis and degradation reactions using synthesize_degrade_table function.

# Code
```

    Specify synthesis and degradation reactions for A and B in a table::

        Model()
        Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        Monomer('B', ['x'])
        synthesize_degrade_table([[A(x=None, y='e'), 1e-4, 1e-6],
                                  [B(),              None, 1e-7]])

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        >>> Monomer('B', ['x'])
        Monomer('B', ['x'])
        >>> synthesize_degrade_table([[A(x=None, y='e'), 1e-4, 1e-6],
        ...                           [B(),              None, 1e-7]]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
            Rule('synthesize_Ae', None >> A(x=None, y='e'), synthesize_Ae_k),
            Parameter('synthesize_Ae_k', 0.0001),
            Rule('degrade_Ae', A(x=None, y='e') >> None, degrade_Ae_k),
            Parameter('degrade_Ae_k', 1e-06),
            Rule('degrade_B', B() >> None, degrade_B_k),
            Parameter('degrade_B_k', 1e-07),

```
