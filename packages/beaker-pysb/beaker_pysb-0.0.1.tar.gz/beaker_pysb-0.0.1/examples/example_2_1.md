# Description
Creating a subclass of the Builder class to implement custom macros or motifs for combinatorial model building.

# Code
```
from pysb import *

class Builder(object):
    def __init__(self, params_dict=None):
        self.model = Model('model', _export=False)
        self.estimate_params = []
        self.params_dict = params_dict
        self.priors = []

    def monomer(self, *args, **kwargs):
        m = Monomer(*args, _export=False, **kwargs)
        self.model.add_component(m) 
        return m

    def parameter(self, name, value, factor=1, prior=None):
        if self.params_dict is None:
            param_val = value * factor
        else:
            if name in self.params_dict:
                param_val = self.params_dict[name] * factor
            else:
                param_val = value * factor

        p = Parameter(name, param_val, _export=False)
        self.model.add_component(p)

        if prior is not None:
            self.estimate_params.append(p)
            self.priors.append(prior)

        return p

    def rule(self, *args, **kwargs):
        r = Rule(*args, _export=False, **kwargs)
        self.model.add_component(r)
        return r

    def compartment(self, *args, **kwargs):
        c = Compartment(*args, _export=False, **kwargs)
        self.model.add_component(c)
        return c

    def observable(self, *args, **kwargs):
        o = Observable(*args, _export=False, **kwargs)
        self.model.add_component(o)
        return o

    def expression(self, *args, **kwargs):
        e = Expression(*args, _export=False, **kwargs)
        self.model.add_component(e)
        return e

    def energypattern(self, *args, **kwargs):
        p = EnergyPattern(*args, _export=False, **kwargs)
        self.model.add_component(p)
        return p

    def initial(self, *args, **kwargs):
        i = Initial(*args, _export=False, **kwargs)
        self.model.add_initial(i)
        return i

    def tag(self, *args, **kwargs):
        t = Tag(*args, _export=False, **kwargs)
        self.model.add_component(t)
        return t

    def __getitem__(self, index):

    class MyBuilder(pysb.builder.Builder):
        # Constructor with monomer declarations, etc....

        def my_motif():
            k1 = self.parameter('k1', 1, _estimate=False)
            k2 = self.parameter('k2', 1, prior=Uniform(-5, -1))
            A = self['A']
            B = self['B']
            self.rule('A_B_bind', A(b=None) + B(b=None) | A(b=1) % B(b=1),

```
