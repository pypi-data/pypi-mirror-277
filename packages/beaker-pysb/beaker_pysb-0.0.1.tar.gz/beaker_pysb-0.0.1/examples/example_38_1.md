# Description
This example demonstrates how to integrate and plot the trajectories of a model using the `ScipyOdeSimulator` from the `pysb` library. It simulates the Robertson model over a time span from t=0 to t=40 and then plots the normalized trajectories of three observables: 'A_total', 'B_total', and 'C_total'.

# Code
```
matplotlib.pyplot import plot, legend, show
numpy import linspace, array
pysb.simulator import ScipyOdeSimulator

# We will integrate from t=0 to t=40
t = linspace(0, 40)
# Simulate the model
print("Simulating...")
y = ScipyOdeSimulator(model, integrator_options=dict(rtol=1e-4, atol=[1e-8, 1e-14, 1e-6])).run(
    tspan=t).all
# Gather the observables of interest into a matrix
yobs = array([y[obs] for obs in ('A_total', 'B_total', 'C_total')]).T
# Plot normalized trajectories
plot(t, yobs / yobs.max(0))
legend(['y1', 'y2', 'y3'], loc='lower right')

```
