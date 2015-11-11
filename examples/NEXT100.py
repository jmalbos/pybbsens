###

import os.path
import sys
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(FILE_PATH + '/..')

from pybbsens import units
from pybbsens import isotope
from pybbsens import experiment
from pybbsens import conflimits
from pybbsens import nmeset


name = "NEXT100"
eff  = 0.3
eres = isotope.Xe136.Qbb * 0.0075
bkg  = 5.E-4 / (units.keV*units.kg*units.year)
mass = 91. *units.kg
expo = mass * 3 * units.year

NEXT100 = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)

FCM = conflimits.FCMemoizer(90)
FCM.ReadTableAverageUpperLimits()

nmes=["ISM","IBM2","QRPA_Tu","QRPA_Jy","EDF"]
for nme in nmes:
	print "NME = ", nme
	isotope.SelectNMESet(nmeset.nmedb[nme])

	mbb = NEXT100.sensitivity_mbb(expo,FCM)
	print "mbb (meV) =",mbb /units.meV
	hl = NEXT100.sensitivity_halflife(expo, FCM)
	print "Tonu (year) =",hl / units.year