# Description
This example demonstrates how to use the SpeciesPatternMatcher to check species fired by reactant patterns. It includes assertions to verify the proper behavior of the patterns.

# Code
```
pysb.pattern import SpeciesPatternMatcher
pysb.examples import bax_pore
pysb.bng import generate_equations
pysb import as_reaction_pattern, WILD, ANY

def test_species_pattern_matcher():
    # See also SpeciesPatternMatcher doctests

    # Check that SpeciesPatternMatcher raises exception if model has no species
    model = robertson.model
    model.reset_equations()
    assert_raises(Exception, SpeciesPatternMatcher, model)

    model = bax_pore.model
    generate_equations(model)
    spm = SpeciesPatternMatcher(model)
    BAX = model.monomers['BAX']
    sp_sets = spm.species_fired_by_reactant_pattern(
        as_reaction_pattern(BAX(t1=None, t2=None))
    )
    assert len(sp_sets) == 1
    assert len(sp_sets[0]) == 2

    sp_sets = spm.species_fired_by_reactant_pattern(
        as_reaction_pattern(BAX(t1=WILD, t2=ANY))
    )
    assert len(sp_sets) == 1

```
