# Description
Defines the binding rules for ligand-receptor and other molecular interactions, along with their respective rate parameters, forming the core dynamics of the model.

# Code
```
from pysb import *
Model()

Parameter('L_0', 1500e3)
Parameter('pR_0', 170.999e3)
Parameter('FADD_0', 133.165e3)
Parameter('flipL_0', 0.49995e3)
Parameter('flipS_0', 0.422e3)
Parameter('pC8_0', 200.168e3)
Parameter('Bid_0', 100e3)
Monomer('L', ['b'])
Monomer('pR', ['b', 'rf'])
Monomer('FADD', ['rf', 'fe'])
Monomer('flipL', ['b', 'fe', 'ee', 'D384'], {'D384': ['U', 'C']})
Monomer('flipS', ['b', 'fe', 'ee'])
Monomer('pC8', ['fe', 'ee', 'D384', 'D400'], {'D384': ['U', 'C'], 'D400': ['U', 'C']})
Monomer('Bid')
Monomer('tBid')

# L + R <--> L:R
Parameter('kf1', 70.98e-03) #70.98e-03
Parameter('kr1', 0)
Rule('R_L_Binding', L (b=None) + pR (b=None, rf=None) >> L (b=1) % pR (b=1, rf=None), kf1)

# FADD binds
Parameter('kf29', 84.4211e-03) #84.4211e-03
Rule('RL_FADD_Binding', pR (b=ANY, rf=None) + FADD (rf=None, fe=None) >> pR (b=ANY, rf=2) % FADD (rf=2, fe=None), kf29)

#C8 binds to L:R:FADD
Parameter('kf30', 3.19838e-03) #3.19838e-03
Parameter('kr30', 0.1) #0.1
Rule('RLFADD_C8_Binding', FADD (rf=ANY, fe=None) + pC8 (fe=None, ee=None, D384='U') | FADD (rf=ANY, fe=1) % pC8 (fe=1, ee=None, D384='U'), kf30, kr30)

#FLIP(variants) bind to L:R:FADD
Parameter('kf31', 69.3329e-03)
Parameter('kr31', 0.0)
Parameter('kf32', 69.4022e-03)
Parameter('kr32', 0.08)
# FIXME: this pattern requires a dummy kr31 which is ultimately ignored
for flip_m, kf, kr, reversible in (zip(flip_monomers, (kf31,kf32), (kr31,kr32), (False,True))):
    rule = Rule('RLFADD_%s_Binding' % flip_m.name, FADD (rf=ANY, fe=None) + flip_m (fe=None, ee=None) | FADD (rf=ANY, fe=1) % flip_m (fe=1, ee=None), kf, kr)
    if reversible is False:
        rule.is_reversible = False
        rule.rule_expression.is_reversible = False
        rule.rate_reverse = None

pC8_HomoD   = pC8 (fe=ANY, ee=1, D384='U') % pC8   (fe=ANY, ee=1, D384='U')
pC8_HeteroD = pC8 (fe=ANY, ee=1, D384='U') % flipL (fe=ANY, ee=1, D384='U')
p43_HomoD   = pC8 (fe=ANY, ee=1, D384='C') % pC8   (fe=ANY, ee=1, D384='C')
p43_HeteroD = pC8 (fe=ANY, ee=1, D384='C') % flipL (fe=ANY, ee=1, D384='C')

#L:R:FADD:C8 dimerizes
Parameter('kf33', 2.37162)
Parameter('kr33', 0.1)
Parameter('kc33', 1e-05)
Rule('RLFADD_C8_C8_Binding', pC8 (fe=ANY, ee=None, D384='U') + pC8 (fe=ANY, ee=None, D384='U') | pC8_HomoD, kf33, kr33)

#L:R:FADD:C8 L:R:FADD:FLIP(variants) dimerizes
Parameter('kf34', 4.83692)
Parameter('kr34', 0)
Parameter('kf35', 2.88545)
Parameter('kr35', 1)
# FIXME: this pattern requires a dummy kr31 which is ultimately ignored
for flip_m, kf, kr, reversible in (zip(flip_monomers, (kf34,kf35), (kr34,kr35), (False,True))):
    rule = Rule('RLFADD_C8_%s_Binding' % flip_m.name, pC8 (fe=ANY, ee=None, D384='U') + flip_m (fe=ANY, ee=None) | pC8 (fe=ANY, ee=1, D384='U') % flip_m (fe=ANY, ee=1), kf, kr)
    if reversible is False:
        rule.is_reversible = False
        rule.rule_expression.is_reversible = False
        rule.rate_reverse = None

Parameter('kc36', 0.223046e-3)
#Homodimer catalyses Homodimer ?: no p18 is released. Only this "cleaved" p43 homoD is the product that will transform into a p18 + L:R:FADD in later reaction.
Rule('HomoD_cat_HomoD', pC8_HomoD + pC8_HomoD >> pC8_HomoD + p43_HomoD, kc36)
#Homodimer catalyses Heterodimer ?????
Rule('HomoD_cat_HeteroD', pC8_HomoD + pC8_HeteroD >> pC8_HomoD + p43_HeteroD, kc36)

Parameter('kc37', 0.805817e-3)
#Heterodimer catalyses Heterodimer ?????
Rule('HeteroD_cat_HeteroD', pC8_HeteroD + pC8_HeteroD >> pC8_HeteroD + p43_HeteroD, kc37)
#Heterodimer catalyses Homodimer ?????
Rule('HeteroD_cat_HomoD', pC8_HeteroD + pC8_HomoD >> pC8_HeteroD + p43_HomoD, kc37)

Parameter('kc38', 1.4888e-3)
#Cleaved Homodimer catalyses Homodimer ?????
Rule('Cl_HomoD_cat_HomoD', p43_HomoD + pC8_HomoD >> p43_HomoD + p43_HomoD, kc38)
#Cleaved HomoD catalyses Heterodimer ?????
Rule('Cl_HomoD_cat_HeteroD', p43_HomoD + pC8_HeteroD >> p43_HomoD + p43_HeteroD, kc38)

Parameter('kc39', 13.098e-3)
#Cleaved HeteroD catalyses Homodimer ?????
Rule('Cl_heteroD_cat_HomoD', p43_HeteroD + pC8_HomoD >> p43_HeteroD + p43_HomoD, kc39)
#Cleaved HeteroD catalyses Heterodimer ?????
Rule('Cl_heteroD_cat_HeteroD', p43_HeteroD + pC8_HeteroD >> p43_HeteroD + p43_HeteroD, kc39)

#Cleaved HomoD catalyses Cleaved HomoD to p18 and release L:R:FADD
Parameter('kc40', 0.999273e-3)
Rule('Cl_HomoD_cat_Cl_HomoD', pC8 (fe=ANY, ee=1, D384='C', D400='U') % pC8 (fe=ANY, ee=1, D384='C', D400='U') +
     FADD (rf=ANY, fe=2) % pC8 (fe=2, ee=3, D384='C', D400='U') % FADD (rf=ANY, fe=4) % pC8 (fe=4, ee=3, D384='C', D400='U') >>
     pC8 (fe=ANY, ee=1, D384='C', D400='U') % pC8 (fe=ANY, ee=1, D384='C', D400='U') +
     FADD (rf=ANY, fe=None) + FADD (rf=ANY, fe=None) + pC8 (fe=None, ee=1, D384='C',D400='C') % pC8 (fe=None, ee=1, D384='C',D400='C'), 
     kc40)

#Cleaved HeteroD catalyses Cleaved HomoD to p18 and release L:R:FADD
Parameter('kc41', 0.982109e-3)
Rule('Cl_HeteroD_cat_Cl_HomoD', pC8 (fe=ANY, ee=1, D384='C', D400='U') % flipL (fe=ANY, ee=1, D384='C') +
     FADD (rf=ANY, fe=2) % pC8 (fe=2, ee=3, D384='C', D400='U') % FADD (rf=ANY, fe=4) % pC8 (fe=4, ee=3, D384='C', D400='U') >>
     pC8 (fe=ANY, ee=1, D384='C', D400='U') % flipL (fe=ANY, ee=1, D384='C') +
     FADD (rf=ANY, fe=None) + FADD (rf=ANY, fe=None) + pC8 (fe=None, ee=1, D384='C',D400='C') % pC8 (fe=None, ee=1, D384='C',D400='C'), 
     kc41)
 
#Cleaved HomoD cleaves Bid ?????
Parameter('kc42', 0.0697394e-3)
Rule('Cl_Homo_cat_Bid', pC8 (fe=ANY, ee=1, D384='C', D400='U') % pC8 (fe=ANY, ee=1, D384='C', D400='U') + Bid () >>
     pC8 (fe=ANY, ee=1, D384='C', D400='U') % pC8 (fe=ANY, ee=1, D384='C', D400='U') + tBid (), kc42)

#Cleaved HeteroD cleaves Bid ?????
Parameter('kc43', 0.0166747e-3)
Rule('Cl_Hetero_cat_Bid', pC8 (fe=ANY, ee=1, D384='C', D400='U') % flipL (fe=ANY, ee=1, D384='C') + Bid () >>
     pC8 (fe=ANY, ee=1, D384='C', D400='U') % flipL (fe=ANY, ee=1, D384='C') + tBid (), kc43)

#p18 cleaves Bid ?????
Parameter('kc44', 0.0000479214e-3)
Rule('p18_Bid_cat', pC8 (fe=None, ee=1, D384='C',D400='C') % pC8 (fe=None, ee=1, D384='C',D400='C') + Bid () >> 

```
