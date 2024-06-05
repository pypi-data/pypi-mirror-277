# Description
Run a stochastic simulation on the model from expression_observables and verify the output time points.

# Code
```
pysb.simulator import StochKitSimulator
pysb.examples import expression_observables

def test_stochkit_expressions():
    model = expression_observables.model
    tspan = np.linspace(0, 100, 11)
    sim = StochKitSimulator(model, tspan=tspan)

```
