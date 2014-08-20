### This script calculates the sensitivity of an experiment searching
### for 0nubb-decay in Ge76 

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'
import sys
sys.path.append(FILE_PATH + '/..')
import matplotlib.pyplot as plt

import csv
from numpy import arange
from pybbsens import units
from pybbsens import isotope
from pybbsens import experiment
from pybbsens import conflimits
from pybbsens import nmeset

isotope.SelectNMESet(nmeset.nmedb['QRPA_Jy'])


########################################
### EXPERIMENT DATA ####################

name = "GeFuture"
isot = isotope.Ge76
eff  = 0.62
eres = isot.Qbb * 0.0015
bkg  = 1E-3 / (units.keV*units.kg*units.year)
mass = 500. *units.kg               #dummy
expo = 2000 *units.kg*units.year    #dummy

nmes=["ISM","IBM2","QRPA_Tu","QRPA_Jy","EDF"]


########################################
### Create a confidence-limit calculator. 
### We use in this case the Feldman-Cousins memoizer.
fcm = conflimits.FCMemoizer(0.9)
fcm.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

exp = experiment.Experiment(name, isotope.Ge76, eff, eres, bkg, mass)

for nme in nmes:
	filename = 'GeExp_' + nme + '.txt'
	writer = csv.writer(open(filename, 'w'))

	isotope.SelectNMESet(nmeset.nmedb[nme])
	for exposure in arange(100., 10010., 10.):
		exposure = exposure * units.kg * units.year
		mbb = exp.sensitivity(exposure, fcm) / units.meV
		exposure = exposure / (units.kg*units.year)
		writer.writerow([exposure,mbb])
