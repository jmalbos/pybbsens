"""docstring for experiment"""

import isotope
import units
import constants

import math



class Experiment(object):
    """docstring for Experiment"""

    def __init__(self, name, isotope, eff, res, bkg, mass):
        super(Experiment, self).__init__()
        self.name = name
        self.isotope = isotope
        self.eff = eff
        self.res = res
        self.bkg = bkg
        self.mass = mass

    def Nbb(self, time, halflife):
        """Return the number of bb events expected in the experiment after
        a certain observation time and given a certain half-life."""

        N = math.log(2.) * self.eff * self.mass * constants.N_A * time \
        / (self.isotope.W * halflife)

        return N

    def half_life(self, time, Nbb):
        """Calculate the half-life for a given number of observed events"""

        hl = math.log(2.) * self.eff * self.mass * constants.N_A * time \
        / (self.isotope.W * Nbb)

        return hl


##############################

name = "NEXT100"

eff  = 0.30
res  = 0.75 
bkg  = 5.E-4 /(units.keV*units.kg*units.year)
mass = 100.*0.91*units.kg

next100 = Experiment(name, isotope.Xe136, eff, res, bkg, mass)

##############################

name = "EXO200"

eff  = 0.50
res  = 4.0
bkg  = 1.7E-3 / (units.keV*units.kg*units.year)
mass = 200.*0.81*units.kg

exo200 = Experiment(name, isotope.Xe136, eff, res, bkg, mass)

##############################


if __name__ == '__main__':

    print next100.Nbb(5*units.year, 1.E25*units.year)