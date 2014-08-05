"""docstring for module nmeset"""


class NMESet(object):
    """docstring for NMESet"""
    def __init__(self, name, g_A, **kwargs):
        super(NMESet, self).__init__()
        self.name = name
        self.g_A = g_A
        self.data = kwargs


############################################################
### NUCLEAR MATRIX ELEMENTS --- DATABASE

### INTERACTING BOSON MODEL (IBM2)
IBM2 = NMESet(name='IBM2', g_A=1.269, Ca48=1.98, Ge76=5.42, Se82=4.37, Zr96=2.53, Mo100=3.73, Pd110=3.62, Cd116=2.78, Sn124=3.50, Te130=4.03, Xe136=3.33, Nd150=2.32)

### INTERACTING SHELL MODEL
ISM = NMESet(name='ISM', g_A=1.25, Ca48=0.54, Ge76=2.22, Se82=2.11, Zr96=0.00, Mo100=0.00, Pd110=0.00, Cd116=0.00, Sn124=2.02, Te130=2.04, Xe136=1.70, Nd150=0.00)

### QUASIPARTICLE RANDOM PHASE APPROXIMATION --- TUBINGEN
QRPA_Tu = NMESet(name='QRPA_Tu', g_A=1.254, Ca48=0.00, Ge76=4.68, Se82=4.17, Zr96=1.34, Mo100=3.53, Pd110=0.00, Cd116=2.93, Sn124=0.00, Te130=3.38, Xe136=2.22, Nd150=0.00)

### QUASIPARTICLE RANDOM PHASE APPROXIMATION --- JYVASKYLA
QRPA_Jy = NMESet(name='QRPA_Jy', g_A=1.25, Ca48=1.67, Ge76=3.83, Se82=3.15, Zr96=2.07, Mo100=2.74, Pd110=4.15, Cd116=3.03, Sn124=3.3, Te130=3.47, Xe136=2.36, Nd150=0.00)

### ENERGY DENSITY FUNCTION (EDF)
EDF = NMESet(name="EDF", g_A=1.25, Ca48=2.23, Ge76=5.55, Se82=4.67, Zr96=6.50, Mo100=6.59, Pd110=0.00, Cd116=5.35, Sn124=5.79, Te130=6.41, Xe136=4.77, Nd150=2.19)

### DICTIONARY
nmedb = {IBM2.name: IBM2, ISM.name: ISM}



#if __name__ == '__main__':
    #print NMEs['IBM2'].g_A

