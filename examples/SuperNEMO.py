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


name = "SuperNEMO"
isot = isotope.Se82
eff  = 0.28 ## Not known for sure
eres = isot.Qbb * 0.0153 * 2.35
bkg  = 5.E-5 / (units.keV*units.kg*units.year)
mass = 100. *units.kg
expo = 18. *units.kg*units.year

EXO200 = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)

FCM = conflimits.FCMemoizer(0.9)
FCM.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

for key in nmeset.nmedb:
	print "NME = ", key
	isotope.SelectNMESet(nmeset.nmedb[key])
	mbb = EXO200.sensitivity(expo,FCM)
	print "mbb (meV) =",mbb /units.year
	hl = isot.half_life(mbb)
	print "Tonu (year) =",hl / units.year