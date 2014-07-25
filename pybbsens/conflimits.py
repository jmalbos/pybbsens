from ROOT import TFeldmanCousins


class ConfLimitsCalculator(object):

    def __init__(self, CL):
        self.CL = CL

    def UpperLimit(self, obs, bkg):
        pass

    def LowerLimit(self, n, b):
        pass

    def AverageUpperLimit(self):
        pass        


class FeldmanCousins(ConfLimitsCalculator):

    def __init__(self, CL):
        super(FeldmanCousins, self).__init__(CL)
        self.FC = TFeldmanCousins(self.CL)
        self.FC.SetMuMax(200.)

    def UpperLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        if obs==self.FC.GetNobserved() and bkg==self.FC.GetNbackground():
            return self.FC.GetUpperLimit()
        else:
            return self.FC.CalculateUpperLimit(obs,bkg)

    def LowerLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        if obs==self.FC.GetNobserved() and bkg==self.FC.GetNbackground():
            return self.FC.GetLowerLimit()
        else:
            return self.FC.CalculateLowerLimit(obs,bkg)

    def AverageUpperLimit(bkg):
        """
        For a number of events b, compute the average upper limit. That is:
        U = Sum Po(n;b) * Upper (n,b)
        """


