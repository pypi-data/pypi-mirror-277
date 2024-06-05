# Description
Simulating and plotting kinase cascade dynamics using PySB and Matplotlib.

# Code
```
__future__ import print_function
pysb.simulator import ScipyOdeSimulator
matplotlib.pyplot import plot, legend, show
matplotlib.pylab import linspace

tspan = linspace(0, 1200)
print("Simulating...")
yfull = ScipyOdeSimulator(model).run(tspan=tspan).all
plot(tspan, yfull['ppMEK'], label='ppMEK')
plot(tspan, yfull['ppERK'], label='ppERK')
legend(loc='upper left')

```
