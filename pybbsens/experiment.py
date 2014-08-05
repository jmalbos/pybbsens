"""docstring for experiment"""

import isotope
import units
import constants
import conflimits

import math



class Experiment(object):
    """docstring for Experiment"""

    def __init__(self, name, isotope, eff, res, bkg, mass):
        self.name = name ### Experiment's name
        self.isotope = isotope ### bb isotope used by the experiment
        self.eff = eff ### Detection efficiency for 0nubb
        self.res = res ### Energy resolution (% FWHM) at Qbb
        self.bkg = bkg ### Background rate in ROI
        self.mass = mass ### Isotope mass

    def N2nubb(self, time):
        """Return the number of 2nubb expected after a certain 
        observation time assuming perfect detection efficiency."""
        return math.log(2.) * self.mass * constants.N_A * time \
               / (self.isotope.W * self.isotope.T2nu)

    def mbb(self, half_life):
        """Return the neutrino Majorana mass corresponding to a given half-life
        of the 0nubb decay"""


    def sensitivity(self, exposure):
        bevts = self.bkg * exposure * self.res
        #AUL = conflimits.FeldmanCousins().AverageUpperLimit(bevts)
        AUL=3.
        A = math.sqrt(self.isotope.W * constants.m_e**2 / (constants.N_A * math.log(2.) * self.isotope.G0nu * 2.**2))

        return A*math.sqrt(AUL/(self.eff*exposure))




##############################

name = "NEXT100"

eff  = 0.30
res  = 0.75*2458.*units.keV 
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

    print next100.N2nubb(5*units.year)
    #print next100.sensitivity(100.*units.kg*units.year) / units.meV