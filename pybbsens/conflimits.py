"""docstring for module conflimits"""

import math
import numpy
import csv
from ROOT import TFeldmanCousins
from scipy.stats import poisson


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

    def __init__(self, CL=0.9):
        super(FeldmanCousins, self).__init__(CL)
        self.FC = TFeldmanCousins(self.CL)
        self.FC.SetMuMax(200.)

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

    def __init__(self, CL=0.90):
        super(FCMemoizer, self).__init__(CL)

    def ComputeTableAverageUpperLimits(self, bmin, bmax, step, filename):
        """Compute a lookup table of average upper limits."""

        writer = csv.writer(open(filename, 'w'))

        brange = numpy.arange(bmin, bmax, step)

        for b in brange:
            UL = super(FCMemoizer, self).AverageUpperLimit(b)
            writer.writerow([b,UL])



            


if __name__ == '__main__':

    fccl = FeldmanCousins()
    print fccl.UpperLimit(0.,0.)
    print fccl.AverageUpperLimit(15.)

    #fcm = FCMemoizer()
    #fcm.ComputeTableAverageUpperLimits(0.,15., 1., 'fc09.dat')

