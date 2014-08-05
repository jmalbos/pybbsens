"""Physical constants of use in the sensitivity calculations."""

import units

### Avogadro constant
Avogadro = 6.02214129E+23 * (1./units.mole)
N_A = Avogadro

### Electron mass
electron_mass = 0.510998928 * units.MeV
m_e = electron_mass