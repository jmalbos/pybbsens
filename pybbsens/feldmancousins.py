"""docstring for feldmancousins module"""

import math
from scipy.stats import poisson
from ROOT import TFeldmanCousins


class FeldmanCousins(object):
    """docstring for FeldmanCousins"""

    def __init__(self, CL=0.9):
        super(FeldmanCousins, self).__init__()
        self.fc = TFeldmanCousins(CL)
        self.fc.SetMuMax(200.)

    def AverageUpperLimit(self, b):
        """Compute the average upper limit for a Poisson distribution 
        of mean b: <UL> = \sum Po(n;b) U(n;b)."""

        sigma = math.sqrt(b)
        nmin = int(max(0.,  b-4.*sigma))
        nmax = int(max(20., b+4.*sigma)+1.)

        print "nmin, nmax = ", nmin, nmax

        po = poisson(b)

        print "CDF(nmin) = ", po.cdf(nmin)
        print "CDF(nmax-inf) = ", 1.-po.cdf(nmax)

        UL = 0.

        for i in range(nmin, nmax):

            print 'i = ', i
            print 'Po(i) = ', po.pmf(i)
            print 'U(i,b) = ', self.fc.CalculateUpperLimit(i,b)

            UL += po.pmf(i) * self.fc.CalculateUpperLimit(i,b)

        return UL


if __name__ == '__main__':

    FC = FeldmanCousins(0.95)
    print FC.AverageUpperLimit(99.5)
