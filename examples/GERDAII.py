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


name = "GERDAII"
isot = isotope.Ge76
eff  = 0.62
eres = isot.Qbb * 0.0015
bkg  = 1.0E-3 / (units.keV*units.kg*units.year)
mass = 50. *units.kg
expo = 200. *units.kg*units.year

GERDA = experiment.Experiment(name, isotope.Ge76, eff, eres, bkg, mass)

FCM = conflimits.FCMemoizer(0.9)
FCM.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

nmes=["ISM","IBM2","QRPA_Tu","QRPA_Jy","EDF"]
for nme in nmes:
	print "NME = ", nme
	isotope.SelectNMESet(nmeset.nmedb[nme])

	mbb = GERDA.sensitivity(expo,FCM)
	print "mbb (meV) =",mbb /units.meV
	hl = isot.half_life(mbb)
	print "Tonu (year) =",hl / units.year
