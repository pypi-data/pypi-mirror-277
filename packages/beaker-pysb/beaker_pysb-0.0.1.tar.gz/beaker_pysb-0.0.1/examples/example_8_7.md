# Description
Generate the reversible binding reaction DRUG + SUBSTRATE | DRUG:SUBSTRATE that only gets triggered when the simulation reaches the time point t_action using drug_binding function.

# Code
```

    Binding between drug and substrate::
        Model()
        Monomer('drug', ['b'])
        Monomer('substrate', ['b'])
        drug_binding(drug(), 'b', substrate(), 'b', 10, [2,4])

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('drug', ['b'])
        Monomer('drug', ['b'])
        >>> Monomer('substrate', ['b'])
        Monomer('substrate', ['b'])
        >>> drug_binding(drug(), 'b', substrate(), 'b', 10, [0.1, 0.01])
        ComponentSet([
         Rule('bind_drug_substrate_to_drugsubstrate', drug(b=None) + substrate(b=None) | drug(b=1) % substrate(b=1), kf_expr_drug_substrate, kr_expr_drug_substrate),
         Parameter('kf_drug_substrate', 0.1),
         Parameter('kr_drug_substrate', 0.01),
         Rule('synthesize___t', None >> __t(), __k_t),
         Monomer('__t'),
         Parameter('__k_t', 1.0),
         Observable('t', __t()),
         Expression('kf_expr_drug_substrate', Piecewise((kf_drug_substrate, t > 10), (0, True))),
         Expression('kr_expr_drug_substrate', Piecewise((kr_drug_substrate, t > 10), (0, True))),

```
