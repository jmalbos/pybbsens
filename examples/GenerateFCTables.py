"""This script expects to be living within the 'examples' directory
of the pybbsens distribution."""

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'

import sys
sys.path.append(FILE_PATH + '/..')

from pybbsens import conflimits


def GenerateFCTable(CL, bkg_min=0., bkg_max=100., step=1.0):
    """Generate a table of Feldman-Cousins average upper limits 
    between bkg_min and bkg_max for a given confidence level (CL)."""

    filename = DATA_PATH + 'FC' + str(int(CL*100)) + '.dat'

    print 'Generating table of Feldman-Cousins average upper values for CL=%0.2f' % CL
    
    fcm = conflimits.FCMemoizer(CL)
    fcm.ComputeTableAverageUpperLimits(bkg_min, bkg_max, step, filename)


if __name__ == '__main__':
    
    GenerateFCTable(0.68)
    GenerateFCTable(0.90)
    GenerateFCTable(0.95)
    GenerateFCTable(0.99)
