import numpy as np
import matplotlib.pyplot as plt

from scipy.constants import m_e, m_p, pi

fsize = 12

mi = m_p*39.948  # argon

def phi_Te(g):
  return g/(g-1)*( 1 - (2*pi*g*m_e/mi)**((g-1)/(g+1)))

gg = np.linspace(0.9,1.7, 80)

f, ax = plt.subplots(1, 1, figsize = (6.4, 4))
plt.subplots_adjust(left=0.2, bottom=0.12, right=0.84, top=0.97, wspace=0.0, hspace=.0)

ax.plot(gg, phi_Te(gg), '-k', linewidth = 2)
ax.set_xlabel("$\gamma$", fontsize = fsize)
ax.set_ylabel("$e\phi_s / (k_B T_{e,0})$", fontsize = fsize)
ax.set_ylim(0,5)
ax.set_xlim(1,1.7)
ax.grid()
plt.savefig("phinorm_theory.pdf")


