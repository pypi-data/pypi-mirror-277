# Description
Simulate the bax_pore model and plot the results using PySB and Matplotlib libraries.

# Code
```
__future__ import print_function
matplotlib.pyplot as plt
numpy import linspace
pysb.simulator import ScipyOdeSimulator

t = linspace(0, 100)
print("Simulating...")
x = ScipyOdeSimulator(model).run(tspan=t).all

plt.plot(t, x['BAX4'])
plt.plot(t, x['BAX4_inh'])
plt.legend(['BAX4', 'BAX4_inh'], loc='upper left')

```
