# Description
Assembling a BAX pore complex sequentially and transporting cargo (Smac). This example demonstrates how to use the `assemble_pore_sequential` and `pore_transport` functions from the `pysb.macros` library to model a biological process involving the assembly of a pore and cargo transport.

# Code
```
from pysb import *
from pysb.macros import assemble_pore_sequential, pore_transport, pore_species

Model()

# s1,s2 are ring-formation sites; t is the transport (cargo binding) site
Monomer('Bax', ['s1', 's2', 't'])
Annotation(Bax, 'http://identifiers.org/uniprot/Q07812')
# loc is the location, (m)itochondrion or (c)ytosol; t is the transport site
Monomer('Smac', ['loc', 't'], {'loc': ['m','c']})
Annotation(Smac, 'http://identifiers.org/uniprot/Q9NR28')

Parameter('Bax_0', 8e4)
Parameter('Smac_0', 1e5)
for p in Bax_0, Smac_0:
    Annotation(p, 'http://identifiers.org/doi/10.1371/journal.pcbi.1002482',
               'isDescribedBy')

# Start with monomeric Bax and Smac in the mitochondrion
Initial(Bax(s1=None, s2=None, t=None), Bax_0)
Initial(Smac(loc='m', t=None), Smac_0)

# Maximum number of subunits in a pore
max_size = 6
# Size at which pores are "competent" to transport cargo
min_transport_size = 4

# Build handy rate "sets" (in this formulation, rates don't vary with pore size)
assembly_rates = [[2e-4, 1e-3]] * (max_size - 1)

assemble_pore_sequential(Bax(t=None), 's1', 's2', max_size, assembly_rates)
# Transport Smac
pore_transport(Bax, 's1', 's2', 't', min_transport_size, max_size,
               Smac(loc='m'), 't', Smac(loc='c'), transport_rates)

# Add an observable for each pore size
for size in range(1, max_size + 1):
    Observable('Bax%d' % size, pore_species(Bax, 's1', 's2', size))
# Observe unbound Smac in each compartment
Observable('mSmac', Smac(loc='m', t=None))

```
