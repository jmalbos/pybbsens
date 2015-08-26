"""docstring for module conflimits"""

import math
import array
import numpy
import csv
from ROOT import TFeldmanCousins
from scipy.stats import poisson
from scipy import interpolate
import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'



class ConfLimitsCalculator(object):
    """dosctring for class ConfLimitsCalculator"""

    def __init__(self, CL):
        self.CL = CL

    def UpperLimit(self, obs, bkg):
        pass

    def LowerLimit(self, n, b):
        pass

    def AverageUpperLimit(self):
        pass        



class FeldmanCousins(ConfLimitsCalculator):
    """docstring for class FeldmanCousins"""

    def __init__(self, CL=90):
        super(FeldmanCousins, self).__init__(CL)
        self.FC = TFeldmanCousins(self.CL/100.) # Requires CL as a fraction
        self.FC.SetMuMax(500.)

    def UpperLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        return self.FC.CalculateUpperLimit(obs,bkg)

    def LowerLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        return self.FC.CalculateLowerLimit(obs,bkg)

    def AverageUpperLimit(self, bkg):
        """
        For a number of events b, compute the average upper limit. That is:
        UL = Sum Po(n;b) * Upper (n,b)
        """
        ### The Poisson distribution, Po(n;b), is defined only for b>0.
        ### Therefore, this method returns 0 if bkg is negative, and uses
        ### a number close to 0 for the computation if bkg=0.
        if bkg<0.:
            return 0.
        elif bkg==0.:
            bkg=1.E-5

        ### We'll compute the sum in the range [-5sigma, +5sigma] around
        ### the mean, where sigma is the standard deviation of the Poisson
        ### distribution.
        sigma = math.sqrt(bkg)
        nmin = max(0,  int(bkg-5.*sigma))   # Use 0 if nmin<0
        nmax = max(20, int(bkg+5.*sigma)+1) # Use at least 20 for low means
        #print "nmin=%f, nmax=%f" % (nmin,nmax)

        po = poisson(bkg)
        UL = 0.

        for i in range(nmin, nmax):
            pmf = po.pmf(i)
            ul = self.FC.CalculateUpperLimit(i, bkg)
            #print "i=%i, Po(i)=%f, U(i,b)=%f" % (i, pmf, ul)
            UL += po.pmf(i) * self.FC.CalculateUpperLimit(i,bkg)

        return UL



class FCMemoizer(FeldmanCousins):
    """docstring for FCMemoizer"""

    def __init__(self, CL=90):
        super(FCMemoizer, self).__init__(CL)
        self.AULs = 0

    def ComputeTableAverageUpperLimits(self, bmin, bmax, step, filename):
        """Compute a lookup table of average upper limits."""

        writer = csv.writer(open(filename, 'w'))

        brange = numpy.arange(bmin, bmax, step)

        for b in brange:
            UL = super(FCMemoizer, self).AverageUpperLimit(b)
            writer.writerow([b,UL])

    def AverageUpperLimit(self, bkg):
        """Use tabulated data (or for large values of bkg, a mathematical 
        function extracted from a fit to the data) to speed up the computation
        of the Feldman-Cousins average upper limit for a given background
        prediction."""

        if bkg < 0:
            return 0.
        elif bkg < 100.:
            return self.AULs(bkg)
        else:
            return self.FitFunction(bkg)

    def ReadTableAverageUpperLimits(self, filename=''):

        if filename == '':
            filename = DATA_PATH + 'FC' + str(self.CL) + '.dat'

        try:
            reader = csv.reader(open(filename, 'r'))
            xs = array.array('f')
            ys = array.array('f')
            for row in reader:
                xs.append(float(row[0]))
                ys.append(float(row[1]))
            self.AULs = interpolate.interp1d(xs, ys)
        except IOError:
            print "ERROR: Memoizer file not found!\n"
            raise
        
    def FitFunction(self, x):
        """Returns a value for the Feldman-Cousins average upper limit
        using a mathematical function extracted from a fit to the data."""

        if self.CL==90:
            return 1.225 + 1.7312 * math.sqrt(x)
        else:
            raise ZeroDivisionError


if __name__ == '__main__':

    print "\n| pybbsens.conflimits |\n"

    ##########

    print "# Compute Feldman-Cousins confidence intervals for b=0 and n=0-9.\n"

    fc = FeldmanCousins(90)
    for n in range(10):
        print " n = %i :  [%.2f, %.2f]" % (n, fc.LowerLimit(n,0), fc.UpperLimit(n,0))

    ##########

    print """\n# Compute a lookup table of the average upper limit for CL=68%,
    then use it to calculate the average upper limit for several background 
    predictions.\n"""

    fcm = FCMemoizer(68)
    fcm.ComputeTableAverageUpperLimits(0.5,6.5, 1., 'fcmemoizer.dat')
    fcm.ReadTableAverageUpperLimits('fcmemoizer.dat')
    for b in range(1,6):
        print " b = %i :  %.2f" % (b, fcm.AverageUpperLimit(b))

