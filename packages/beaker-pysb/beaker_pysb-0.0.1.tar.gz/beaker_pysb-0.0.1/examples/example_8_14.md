# Description
Generate rules to assemble a polymer by sequential subunit addition using assemble_polymer_sequential function.

# Code
```

    """Generate rules to assemble a polymer by sequential subunit addition.

    The polymer species are created by sequential addition of `subunit` monomers,
    i.e. larger oligomeric species never fuse together. The polymer structure is
    defined by the `polymer_species` macro.

    Parameters
    ----------
    subunit : Monomer or MonomerPattern
        The subunit of which the polymer is composed.
    site1, site2 : string
        The names of the sites where one copy of `subunit` binds to the next.
    max_size : integer
        The maximum number of subunits in the polymer.
    ktable : list of lists of Parameters or numbers
        Table of forward and reverse rate constants for the assembly steps. The
        outer list must be of length `max_size` - 1, and the inner lists must
        all be of length 2. In the outer list, the first element corresponds to
        the first assembly step in which two monomeric subunits bind to form a
        2-subunit complex, and the last element corresponds to the final step in
        which the `max_size`th subunit is added. Each inner list contains the
        forward and reverse rate constants (in that order) for the corresponding
        assembly reaction, and each of these pairs must comprise solely
        Parameter objects or solely numbers (never one of each). If Parameters
        are passed, they will be used directly in the generated Rules. If
        numbers are passed, Parameters will be created with automatically
        generated names based on `subunit`, `site1`, `site2` and the polymer sizes
        and these parameters will be included at the end of the returned
        component list.
    closed : boolean
        If False (default), assembles a linear (non-circular) polymer. If True,
        assembles a circular ring/pore polymer.

    Notes
    -----

    See documentation for :py:func:`assemble_chain_sequential` and
    :py:func:`assemble_pore_sequential` for examples.

    """
    if len(ktable) != max_size - 1:
        raise ValueError("len(ktable) must be equal to max_size - 1")

    def polymer_rule_name(rule_expression, size):
        react_p = rule_expression.reactant_pattern
        monomer = react_p.complex_patterns[0].monomer_patterns[0].monomer
        return '%s_%d' % (monomer.name, size)

    components = ComponentSet()
    s = polymer_species(subunit, site1, site2, 1, closed=closed)
    for size, klist in zip(range(2, max_size + 1), ktable):
        polymer_prev = polymer_species(subunit, site1, site2, size - 1,
                                       closed=closed)
        polymer_next = polymer_species(subunit, site1, site2, size,
                                       closed=closed)
        name_func = functools.partial(polymer_rule_name, size=size)
        rule_name_base = 'assemble_%s_sequential' % \
                         ('pore' if closed else 'chain')
        components |= _macro_rule(rule_name_base,
                                  s + polymer_prev | polymer_next,
                                  klist, ['kf', 'kr'],
                                  name_func=name_func)

```
