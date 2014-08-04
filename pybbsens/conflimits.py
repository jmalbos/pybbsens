"""docstring for module conflimits"""

import math
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
        U = Sum Po(n;b) * Upper (n,b)
        """
        ### If bkg is negative or zero, the poisson distribution
        ### is not defined. Therefore, return 0 for the first case
        ### and use a number close enough to 0 for the calculation
        ### in the second case.
        if bkg<0.:
            return 0.
        elif bkg==0.:
            bkg=1.E-5

        sigma = math.sqrt(bkg)
        nmin = max(0,  int(bkg-5.*sigma))
        nmax = max(20, int(bkg+5.*sigma)+1)

        print "nmin, nmax = ", nmin, nmax

        po = poisson(bkg)

        while po.cdf(nmin) < 1.E-6:
            nmin += 1

        while (1.-po.cdf(nmax)) < 1.E-6:
            nmax = nmax - 1

        print "nmin, nmax = ", nmin, nmax

        #print "CDF(nmin) = ", po.cdf(nmin)
        #print "CDF(nmax-inf) = ", 1.-po.cdf(nmax)

        UL = 0.

        for i in range(nmin, nmax):

            #print 'i = ', i
            #print 'Po(i) = ', po.pmf(i)
            #print 'U(i,b) = ', self.fc.CalculateUpperLimit(i,b)

            UL += po.pmf(i) * self.FC.CalculateUpperLimit(i,bkg)

        return UL



if __name__ == '__main__':

    fccl = FeldmanCousins()
    print fccl.UpperLimit(0.,0.)
    print fccl.AverageUpperLimit(15.)


