# Description
Generate a reaction which synthesizes a species using synthesize function.

# Code
```

    Synthesize A with site x unbound and site y in state 'e'::

        Model()
        Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        synthesize(A(x=None, y='e'), 1e-4)

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        Monomer('A', ['x', 'y'], {'y': ['e', 'f']})
        >>> synthesize(A(x=None, y='e'), 1e-4) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('synthesize_Ae', None >> A(x=None, y='e'), synthesize_Ae_k),
         Parameter('synthesize_Ae_k', 0.0001),

```
