import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))

import sys
sys.path.append(FILE_PATH + '/..')

from pybbsens import units
from pybbsens import isotope
from pybbsens import experiment
from pybbsens import conflimits

name = "EXO200"
isot = isotope.Xe136
eff  = 0.85
eres = isot.Qbb * 0.015 * 2.35
bkg  = 4.E-3 / (units.keV*units.kg*units.year)
mass = 76. *units.kg
expo = 100. *units.kg*units.year

EXO200 = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)

FC = conflimits.FeldmanCousins(0.9)

mbb = EXO200.sensitivity(expo,FC)
hl = isot.half_life(mbb)

print hl / units.year