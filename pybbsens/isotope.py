"""docstring for module isotope"""

import units
import constants
from nmeset import *
import math



class Isotope(object):
    """docstring for Isotope"""

    def __init__(self, symbol, Z, A, W, Qbb, G0nu, M0nu, T2nu):
        super(Isotope, self).__init__()
        self.symbol = symbol
        self.Z = Z  # atomic number
        self.A = A  # mass number
        self.W = W  # isotopic mass
        self.Qbb = Qbb  # Q value of double beta decay
        self.G0nu = G0nu  # phase-space factor
        self.M0nu = M0nu  # nuclear matrix element
        self.T2nu = T2nu  # half-life of the two-nu mode

    def constant_A(self):
        """Return the value of the constant A for the isotope."""
        try:
            return math.sqrt(self.W * constants.m_e**2 / (constants.N_A * math.log(2.) * self.G0nu * self.M0nu**2))
        except ZeroDivisionError:
            return 0.        

    def mbb(self, half_life):
        """Return the value of the neutrino Majorana mass corresponding to
        a given half-life of the 0nubb decay."""
        try:
            mbb2 = constants.m_e**2 / (self.G0nu * self.M0nu**2 * half_life)
            return math.sqrt(mbb2)
        except ZeroDivisionError:
            return 0.

    def half_life(self, mbb):
        Tinv = self.G0nu * self.M0nu**2 * mbb**2 / constants.m_e**2
        try:
            return 1./Tinv;
        except ZeroDivisionError:
            return 0.



############################################################
### DOUBLE BETA DECAY ISOTOPES --- DATABASE

nmeset_ = nmedb['IBM2'] ### Select your favourite NME set here

##############################
### CALCIUM-48 ###############
symbol = 'Ca48'
W    = 47.95 *units.gram/units.mole
Qbb  = 4263. *units.keV
G0nu = 24.81E-15 /units.year
T2nu = 4.4E19 *units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Ca48 = Isotope(symbol, 20, 48, W, Qbb, G0nu, M0nu, T2nu)

##############################
### GERMANIUM-76 #############
symbol = 'Ge76'
W    = 75.92 *units.gram/units.mole
Qbb  = 2039. *units.keV
G0nu = 2.36E-15 /units.year
T2nu = 1.5E21 *units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Ge76 = Isotope(symbol, 32, 76, W, Qbb, G0nu, M0nu, T2nu)

##############################
### SELENIUM-82 ##############
symbol = 'Se82'
W    = 81.92 *units.gram/units.mole
Qbb  = 2998. *units.keV
G0nu = 10.16E-15 /units.year
T2nu = 0.92E20 *units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Se82 = Isotope(symbol, 34, 82, W, Qbb, G0nu, M0nu, T2nu)

##############################
### ZIRCONIUM-96 #############
symbol = 'Zr96'
W    = 95.91 *units.gram/units.mole
Qbb  = 3346. *units.keV
G0nu = 20.58E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Zr96 = Isotope(symbol, 40, 96, W, Qbb, G0nu, M0nu, T2nu)

##############################
### MOLYBDENUM-100 ###########
symbol = 'Mo100'
W    = 99.91 *units.gram/units.mole
Qbb  = 3034. *units.keV
G0nu = 15.92E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Mo100 = Isotope(symbol, 42, 100, W, Qbb, G0nu, M0nu, T2nu)

##############################
### PALLADIUM-110 ############
symbol = 'Pd110'
W    = 109.91 *units.gram/units.mole
Qbb  = 2018. *units.keV
G0nu = 4.82E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Pd110 = Isotope(symbol, 46, 110, W, Qbb, G0nu, M0nu, T2nu)

##############################
### CADMIUM-116 ##############
symbol = 'Cd116'
W    = 115.90 *units.gram/units.mole
Qbb  = 2814. *units.keV
G0nu = 16.70E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Cd116 = Isotope(symbol, 48, 116, W, Qbb, G0nu, M0nu, T2nu)

##############################
### TIN-124 ##################
symbol = 'Sn124'
W    = 123.91 *units.gram/units.mole
Qbb  = 2287. *units.keV
G0nu = 9.04E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Sn124 = Isotope(symbol, 50, 124, W, Qbb, G0nu, M0nu, T2nu)

##############################
### TELLURIUM-130 ############
symbol = 'Te130'
W    = 129.91 *units.gram/units.mole
Qbb  = 2528. *units.keV
G0nu = 14.22E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Te130 = Isotope(symbol, 52, 130, W, Qbb, G0nu, M0nu, T2nu)

##############################
### XENON-136 ################
symbol = 'Xe136'
W    = 135.91 *units.gram/units.mole
Qbb  = 2458. *units.keV
G0nu = 14.58E-15 /units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Xe136 = Isotope(symbol, 54, 136, W, Qbb, G0nu, M0nu, T2nu)

##############################
### NEODYMIUM-150 ############
symbol = 'Nd150'
W    = 149.92 *units.gram/units.mole
Qbb  = 3371. *units.keV
G0nu = 63.03E-15 /units.year
T2nu = 8.2E18 *units.year
M0nu = nmeset_.g_A**2 * nmeset_.data[symbol]

Nd150 = Isotope(symbol, 60, 150, W, Qbb, G0nu, M0nu, T2nu)

##############################
### DICTIONARY ###############

isotopes = {Ca48.symbol: Ca48, Ge76.symbol: Ge76, Se82.symbol: Se82, 
            Zr96.symbol: Zr96, Mo100.symbol: Mo100, Pd110.symbol: Pd110, 
            Cd116.symbol: Cd116, Sn124.symbol: Sn124, Te130.symbol: Te130, 
            Xe136.symbol: Xe136, Nd150.symbol: Nd150}

############################################################


def SelectNMESet(nmeset):
    """Redefine the nuclear matrix elements of all isotopes in the database
    using a chosen NME set."""
    for symbol in isotopes:
        isotopes[symbol].M0nu = nmeset.g_A**2 * nmeset.data[symbol]



if __name__ == '__main__':

    half_life = 2.8E24 * units.year ### CUORICINO Te-130 upper limit
    mbb = Te130.mbb(half_life) / units.eV

    print "Upper limit on effective Majorana neutrino mass from Te-130: mbb = %.3f eV" % (mbb)
