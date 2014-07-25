"""docstring for module isotope"""

import units
import constants

import math
import os.path as op

import pandas as pd



NMEDB = pd.read_csv(op.join(op.dirname(__file__), 'NMEDatabase.csv'), index_col=0)


class Isotope(object):
    """docstring for Isotope"""

    def __init__(self, symbol, Z, A, W, Qbb, G0nu, NMEs):
        super(Isotope, self).__init__()
        self.symbol = symbol
        self.Z = Z  # atomic number
        self.A = A  # mass number
        self.W = W  # isotopic mass
        self.Qbb = Qbb  # Q value of double beta decay
        self.G0nu = G0nu  # phase-space factor
        self.NMEs = NMEs  # nuclear matrix elements
        self.set_M0nu('IBM2')

    def set_M0nu(self, name):
        self.M0nu = self.NMEs[name] * (NMEDB.loc[name]['g_A'])**2

    def specific_sensitivity(self):
        """docstring"""
        return math.sqrt(self.W * constants.m_e**2 / (constants.N_A \
            * math.log(2.) * self.G0nu * self.M0nu**2))



##############################

symbol = 'Ca48'
W    = 47.95 *units.gram/units.mole
Qbb  = 4263. *units.keV
G0nu = 24.81E-15 /units.year
NMEs = NMEDB[symbol]

Ca48 = Isotope(symbol, 20, 48, W, Qbb, G0nu, NMEs)

##############################

symbol = 'Ge76'
W    = 75.92 *units.gram/units.mole
Qbb  = 2039. *units.keV
G0nu = 2.36E-15 /units.year

Ge76 = Isotope(symbol, 32, 76, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Se82'
W    = 81.92 *units.gram/units.mole
Qbb  = 2998. *units.keV
G0nu = 10.16E-15 /units.year

Se82 = Isotope(symbol, 34, 82, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Zr96'
W    = 95.91 *units.gram/units.mole
Qbb  = 3346. *units.keV
G0nu = 20.58E-15 /units.year

Zr96 = Isotope(symbol, 40, 96, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Mo100'
W    = 99.91 *units.gram/units.mole
Qbb  = 3034. *units.keV
G0nu = 15.92E-15 /units.year

Mo100 = Isotope(symbol, 42, 100, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Pd110'
W    = 109.91 *units.gram/units.mole
Qbb  = 2018. *units.keV
G0nu = 4.82E-15 /units.year

Pd110 = Isotope(symbol, 46, 110, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Cd116'
W    = 115.90 *units.gram/units.mole
Qbb  = 2814. *units.keV
G0nu = 16.70E-15 /units.year

Cd116 = Isotope(symbol, 48, 116, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Sn124'
W    = 123.91 *units.gram/units.mole
Qbb  = 2287. *units.keV
G0nu = 9.04E-15 /units.year

Sn124 = Isotope(symbol, 50, 124, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Te130'
W    = 129.91 *units.gram/units.mole
Qbb  = 2528. *units.keV
G0nu = 14.22E-15 /units.year

Te130 = Isotope(symbol, 52, 130, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Xe136'
W    = 135.91 *units.gram/units.mole
Qbb  = 2458. *units.keV
G0nu = 14.58E-15 /units.year

Xe136 = Isotope("Xe136", 54, 136, W, Qbb, G0nu, NMEDB[symbol])

##############################

symbol = 'Nd150'
W    = 149.92 *units.gram/units.mole
Qbb  = 3371. *units.keV
G0nu = 63.03E-15 /units.year

Nd150 = Isotope(symbol, 60, 150, W, Qbb, G0nu, NMEDB[symbol])

##############################

isotopes = {Ca48.symbol: Ca48, Ge76.symbol: Ge76, Se82.symbol: Se82, 
            Zr96.symbol: Zr96, Mo100.symbol: Mo100, Pd110.symbol: Pd110, 
            Cd116.symbol: Cd116, Sn124.symbol: Sn124, Te130.symbol: Te130, 
            Xe136.symbol: Xe136, Nd150.symbol: Nd150}


if __name__ == '__main__':

    order = {Ca48.symbol: 0, Ge76.symbol: 1, Se82.symbol: 2, 
            Zr96.symbol: 3, Mo100.symbol: 4, Pd110.symbol: 5, 
            Cd116.symbol: 6, Sn124.symbol: 7, Te130.symbol: 8, 
            Xe136.symbol: 9, Nd150.symbol: 10}

    for method in NMEDB.index:

        print '## {} #####'.format(method)

        for i in isotopes:
            isotopes[i].set_M0nu(method)
            print '{} = {}'.format(order[i], isotopes[i].specific_sensitivity() \
                / (units.meV*math.sqrt(units.kg*units.year)) )

