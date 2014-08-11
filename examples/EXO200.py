###

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'
import sys
sys.path.append(FILE_PATH + '/..')

from pybbsens import units
from pybbsens import isotope
from pybbsens import experiment
from pybbsens import conflimits
from pybbsens import nmeset

isotope.SelectNMESet(nmeset.nmedb['ISM'])

name = "EXO200"
isot = isotope.Xe136
eff  = 0.846
eres = isot.Qbb * 0.0153 * 2.35
bkg  = 3.5E-3 / (units.keV*units.kg*units.year)
mass = 76. *units.kg
expo = 100. *units.kg*units.year

EXO200 = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)

FCM = conflimits.FCMemoizer(0.9)
FCM.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

mbb = EXO200.sensitivity(expo,FCM)
print mbb / units.year
hl = isot.half_life(mbb)

print hl / units.year