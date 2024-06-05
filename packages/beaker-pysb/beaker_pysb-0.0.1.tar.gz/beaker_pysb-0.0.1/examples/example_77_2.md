# Description
Test on demand observable evaluation

# Code
```
from pysb.bng import generate_equations
from pysb.pattern import SpeciesPatternMatcher
import collections

def test_simres_observable():
    """ Test on demand observable evaluation """
    models = [tyson_oscillator.model, robertson.model,
              expression_observables.model, earm_1_3.model,
              bax_pore_sequential.model, bax_pore.model,
              bngwiki_egfr_simple.model]
    for model in models:
        generate_equations(model)
        spm = SpeciesPatternMatcher(model)
        for obs in model.observables:
            dyn_obs = spm.match(pattern=obs.reaction_pattern, index=True,
                                counts=True)

            # Need to sort by species numerical order for comparison purposes
            dyn_obs = collections.OrderedDict(sorted(dyn_obs.items()))

            dyn_species = list(dyn_obs.keys())

            if obs.match == 'species':
                dyn_coeffs = [1] * len(dyn_obs)
            else:
                dyn_coeffs = list(dyn_obs.values())

            assert dyn_species == obs.species

```
