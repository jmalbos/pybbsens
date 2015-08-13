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


########################################
### EXPERIMENT DATA ####################

name = "XeExp"
isot = isotope.Xe136
eff  = 0.3
eres = 1
bkg  = 0 / (units.keV*units.kg*units.year)
mass = 0. *units.kg
expo = 0. *units.kg*units.year

nmes=["EDF","ISM"]
cnmes=["red","blue","green","grey"]
linestyles = ['-', '--', '-.', ':']


########################################
### Create a confidence-limit calculator. 
### We use in this case the Feldman-Cousins memoizer.
fcm = conflimits.FCMemoizer(0.90)
fcm.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

isotope.SelectNMESet(nmeset.nmedb["ISM"])
bkg_in_ROI = [x/(units.ton*units.year) for x in [0.,0.1,1.,3.]]
#bkg_in_ROI = [x/(units.ton*units.year) for x in [0.1,1.,3.,10.]]

i=0

for bkg in bkg_in_ROI:
	exp = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)
	linestyle = linestyles[i]
	MBB=[]
	TT=[]
	LMT=arange(-1, 2.1, 0.1)
	EXP=[]
	MT=[]

	for lmt in LMT:
	 	MT.append(10**lmt)
	
	for exposure in MT:
		exposure = exposure * units.ton * units.year
		mbb = exp.sensitivity(exposure, fcm) / units.meV
		T= isotope.Xe136.half_life(mbb*units.meV)/units.year
		exposure = exposure / (units.ton*units.year)
		MBB.append(mbb)
		EXP.append(exposure)
		TT.append(T)  
	color = cnmes[i]

	print EXP
	print MBB
	
	plt.plot(EXP, MBB, color, linewidth=2.5, ls=linestyle)
	ax = plt.subplot(111)
	plt.xlabel('Exposure (ton year)')
	plt.ylabel(r'$m_{\beta\beta}$ (meV)')
	ax.set_xscale('log')
	ax.set_yscale('log')
	plt.grid(True)
	i+=1
plt.show()

i=0
for bkg in bkg_in_ROI:
	linestyle = linestyles[i]
	exp = experiment.Experiment(name, isotope.Xe136, eff, eres, bkg, mass)

	MBB=[]
	TT=[]
	LMT=arange(-1, 2.1, 0.1)
	EXP=[]
	MT=[]

	for lmt in LMT:
	 	MT.append(10**lmt)
	
	for exposure in MT:
		exposure = exposure * units.ton * units.year
		mbb = exp.sensitivity(exposure, fcm) / units.meV
		T= isotope.Xe136.half_life(mbb*units.meV)/units.year
		exposure = exposure / (units.ton*units.year)
		MBB.append(mbb)
		EXP.append(exposure)
		TT.append(T)  
	color = cnmes[i]
	plt.plot(EXP, TT, color, linewidth=2.5, ls=linestyle)
	ax = plt.subplot(111)
	#plt.axis(XA[i])
	plt.xlabel('Exposure (ton year)')
	plt.ylabel(r'$T_{1/2}$ (years)')
	ax.set_xscale('log')
	ax.set_yscale('log')
	plt.grid(True)
	
	i+=1
plt.show()

