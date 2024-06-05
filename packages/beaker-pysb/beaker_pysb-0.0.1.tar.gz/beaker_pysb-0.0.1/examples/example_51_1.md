# Description
Generate PottersWheel code for the ODEs of a PySB model.

# Code
```
import pysb
import pysb.bng
import sympy
import re
from io import StringIO

    def export(self):
        """Generate the PottersWheel code for the ODEs of the PySB model
        associated with the exporter.

        Returns
        -------
        string
            String containing the PottersWheel code for the ODEs.
        """
        if self.model.expressions:
            raise ExpressionsNotSupported()
        if self.model.compartments:
            raise CompartmentsNotSupported()

        output = StringIO()
        pysb.bng.generate_equations(self.model)

        model_name = self.model.name.replace('.', '_')

        ic_values = [0] * len(self.model.odes)
        for ic in self.model.initials:
            ic_values[self.model.get_species_index(ic.pattern)] = ic.value.value

        # list of "dynamic variables"
        pw_x = ["m = pwAddX(m, 's%d', %.17g);" % (i, ic_values[i])
                for i in range(len(self.model.odes))]

        # parameters
        pw_k = ["m = pwAddK(m, '%s', %.17g);" % (p.name, p.value)
                for p in self.model.parameters]

        # equations (one for each dynamic variable)
        # Note that we just generate C code, which for basic math expressions
        # is identical to matlab.  We just have to change 'pow' to 'power'.
        # Ideally there would be a matlab formatter for sympy.
        pw_ode = ["m = pwAddODE(m, 's%d', '%s');" %
                  (i, sympy.ccode(self.model.odes[i]))
                  for i in range(len(self.model.odes))]
        pw_ode = [re.sub(r'pow(?=\()', 'power', s) for s in pw_ode]

        # observables
        pw_y = ["m = pwAddY(m, '%s', '%s');" %
                (obs.name,
                    ' + '.join('%f * s%s' % t
                               for t in zip(obs.coefficients, obs.species)))
                 for obs in self.model.observables]

        # Add docstring, if present
        if self.docstring:
            output.write('% ' + self.docstring.replace('\n', '\n% '))
            output.write('\n')

        output.write('% PottersWheel model definition file\n')
        output.write('%% save as %s.m\n' % model_name)
        output.write('function m = %s()\n' % model_name)
        output.write('\n')
        output.write('m = pwGetEmptyModel();\n')
        output.write('\n')
        output.write('% meta information\n')
        output.write("m.ID          = '%s';\n" % model_name)
        output.write("m.name        = '%s';\n" % model_name)
        output.write("m.description = '';\n")
        output.write("m.authors     = {''};\n")
        output.write("m.dates       = {''};\n")
        output.write("m.type        = 'PW-1-5';\n")
        output.write('\n')
        output.write('% dynamic variables\n')
        for x in pw_x:
            output.write(x)
            output.write('\n')
        output.write('\n')
        output.write('% dynamic parameters\n')
        for k in pw_k:
            output.write(k)
            output.write('\n')
        output.write('\n')
        output.write('% ODEs\n')
        for ode in pw_ode:
            output.write(ode)
            output.write('\n')
        output.write('\n')
        output.write('% observables\n')
        for y in pw_y:
            output.write(y)
            output.write('\n')
        output.write('\n')
        output.write('%% end of PottersWheel model %s\n' % model_name)

```
