"""docstring for module isotope"""

import units

class Isotope(object):
    """docstring for Isotope"""

    def __init__(self, symbol, Z, A, W, Qbb, G0nu):
        super(Isotope, self).__init__()
        self.symbol = symbol
        self.Z = Z  # atomic number
        self.A = A  # mass number
        self.W = W  # isotopic mass
        self.Qbb = Qbb  # Q value of double beta decay
        self.G0nu = G0nu  # phase-space factor


############################################################
### DOUBLE BETA DECAY ISOTOPES

### CALCIUM-48
W    = 47.95 *units.gram/units.mole
Qbb  = 4263. *units.keV
G0nu = 24.81E-15 /units.year

Ca48 = Isotope('Ca48', 20, 48, W, Qbb, G0nu)

### GERMANIUM-76
W    = 75.92 *units.gram/units.mole
Qbb  = 2039. *units.keV
G0nu = 2.36E-15 /units.year

Ge76 = Isotope('Ge76', 32, 76, W, Qbb, G0nu)

### SELENIUM-82
W    = 81.92 *units.gram/units.mole
Qbb  = 2998. *units.keV
G0nu = 10.16E-15 /units.year

Se82 = Isotope('Se82', 34, 82, W, Qbb, G0nu)

### ZIRCONIUM-96
W    = 95.91 *units.gram/units.mole
Qbb  = 3346. *units.keV
G0nu = 20.58E-15 /units.year

Zr96 = Isotope('Zr96', 40, 96, W, Qbb, G0nu)

### MOLYBDENUM-100
W    = 99.91 *units.gram/units.mole
Qbb  = 3034. *units.keV
G0nu = 15.92E-15 /units.year

Mo100 = Isotope('Mo100', 42, 100, W, Qbb, G0nu)

### PALLADIUM-110
W    = 109.91 *units.gram/units.mole
Qbb  = 2018. *units.keV
G0nu = 4.82E-15 /units.year

Pd110 = Isotope('Pd110', 46, 110, W, Qbb, G0nu)

### CADMIUM-116
W    = 115.90 *units.gram/units.mole
Qbb  = 2814. *units.keV
G0nu = 16.70E-15 /units.year

Cd116 = Isotope('Cd116', 48, 116, W, Qbb, G0nu)

### TIN-124
W    = 123.91 *units.gram/units.mole
Qbb  = 2287. *units.keV
G0nu = 9.04E-15 /units.year

Sn124 = Isotope('Sn124', 50, 124, W, Qbb, G0nu)

### TELLURIUM-130
W    = 129.91 *units.gram/units.mole
Qbb  = 2528. *units.keV
G0nu = 14.22E-15 /units.year

Te130 = Isotope('Te-130', 52, 130, W, Qbb, G0nu)

### XENON-136
W    = 135.91 *units.gram/units.mole
Qbb  = 2458. *units.keV
G0nu = 14.58E-15 /units.year

Xe136 = Isotope("Xe136", 54, 136, W, Qbb, G0nu)

### NEODYMIUM-150
W    = 149.92 *units.gram/units.mole
Qbb  = 3371. *units.keV
G0nu = 63.03E-15 /units.year

Nd150 = Isotope('Nd150', 60, 150, W, Qbb, G0nu)


### DICTIONARY

isotopes = {Ca48.symbol: Ca48, Ge76.symbol: Ge76, Se82.symbol: Se82, 
            Zr96.symbol: Zr96, Mo100.symbol: Mo100, Pd110.symbol: Pd110, 
            Cd116.symbol: Cd116, Sn124.symbol: Sn124, Te130.symbol: Te130, 
            Xe136.symbol: Xe136, Nd150.symbol: Nd150}


# if __name__ == '__main__':


