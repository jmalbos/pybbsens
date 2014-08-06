### This script generates a table with the constant A for all isotopes
### for a given NME calculation method.
### N.B. The script expects to be living within the folder 'examples' 
### of the pybbsens distribution.

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))

import sys
sys.path.append(FILE_PATH + '/..')

from pybbsens import isotope
from pybbsens import nmeset
from pybbsens import units
import math

isodb = isotope.isotopes
isotope.SelectNMESet(nmeset.nmedb['ISM']) #<< Choose here your favourite method

print "Isotope\t A [meV (kg yr)^-1/2]"
print "--------------------------------"

for symbol in isodb:
    A = isodb[symbol].constant_A() / (units.meV * math.sqrt(units.kg*units.year))
    print "%s\t %.0f" % (symbol, A)
