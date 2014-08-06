### This script calculates the sensitivity of an experiment searching
### for 0nubb-decay in Xe-136 in terms of several background assumptions.
### N.B. The scripts expects to be located in the directory 'examples'
### during the execution.

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'
import sys
sys.path.append(FILE_PATH + '/..')

import csv
from numpy import arange
from pybbsens import units
from pybbsens import isotope
from pybbsens import experiment
from pybbsens import conflimits


########################################
### EXPERIMENT DATA ####################

### The following parameters are not relevant for this calculation.
### Choose dummy values.
eff  = 1.
res  = 1. * units.keV
mass = 0.

### Background counts in ROI per unit of exposure
bkg_in_ROI = [x/(units.kg*units.year) for x in [0.01, 0.001, 0.]]

########################################
### Create a confidence-limit calculator. 
### We use in this case the Feldman-Cousins memoizer.
fcm = conflimits.FCMemoizer(0.9)
fcm.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')


########################################
### Loop now over the different cases, calculating the sensitivity

for b in bkg_in_ROI:

    filename = 'XeExp_' + str(b*(units.kg*units.year)) + '.txt'
    writer = csv.writer(open(filename, 'w'))

    exp = experiment.Experiment("XeExp", isotope.Xe136, eff, res, b/res, mass)

    for exposure in arange(10., 10010., 10.):
        exposure = exposure * units.kg * units.year
        mbb = exp.sensitivity(exposure, fcm) / units.meV
        exposure = exposure / (units.kg*units.year)
        writer.writerow([exposure,mbb])
