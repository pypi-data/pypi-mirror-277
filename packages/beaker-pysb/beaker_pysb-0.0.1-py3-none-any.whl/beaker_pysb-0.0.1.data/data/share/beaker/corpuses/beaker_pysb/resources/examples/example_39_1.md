# Description
This example demonstrates how to simulate a model using the ScipyOdeSimulator from the PySB library. It shows the complete process from importing necessary modules, defining the time span for the simulation, running the simulation, and printing the resulting species concentrations.

# Code
```
__future__ import print_function
pysb.simulator import ScipyOdeSimulator

t = [0, 10, 20, 30, 40, 50, 60]
simulator = ScipyOdeSimulator(model, tspan=t)
simresult = simulator.run()

```
