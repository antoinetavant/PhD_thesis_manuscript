
import pickle
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator
minorLocator = AutoMinorLocator()

data_all = pickle.load( open( "save_data_all.p", "rb" ) )
sigma_0 = 0.5
sigma_max = 2.9
epsilon_0 = 8.85E-12
mi=131*1.67e-27
me=9e-31

q=1.6e-19
qe=q


def simpleplot(name,label = None, datadict = data_all, irang = None, mask = None, norm = False):
    
    toplot = datadict[name].copy()
    
    if norm:
        toplot /= toplot.max()
    
    if label is None:
        label = name
    x = datadict["x"]
    
    plt.plot(x, toplot, label = label)
    plt.xlabel("Radial position $[cm]$")
    plt.legend()
    if irang is not None:
        plt.xlim(irang)
        
    plt.xlabel("Radial position $r [cm]$")
    plt.gca().xaxis.set_minor_locator(minorLocator)
    plt.tick_params( right = True)
    plt.tick_params(which='minor', length=4, color='r')
    
    
def ne_Bolz(phi, n0, T0):
    """Simple model for the electron density
    Bolzmann electrons
    $n_e = n_0 \exp( - \phi/T_e)
    """
    
    phisift = phi - phi.max()
    return n0*np.exp(phisift/T0)

def Te_eff_calcl(sigma, epsi):
    """inverses the linear calculation of sigma for a Maxwellian
    """
    return (sigma - sigma_0)/(1 - sigma_0) * epsi/2

def phi_drop(Te, sigma):
    """Sheath and pre-sheath drop for SEE"""
    phi = Te * np.log((1. - sigma) * np.sqrt(mi / (2. * np.pi * me))
                      ) + Te * 0.5  # [V] plasma potential
    return phi

def sigma_maxw_unsat(Te, epsi):
    return sigma_0 + 2.0*(Te)*(1.0 - sigma_0)/epsi

def sigma_maxw_sat(Te, epsi):
    "SEE rate with saturation"
    AR2    = (sigma_max - sigma_0)/(1- sigma_0) *epsi/Te
    # AR2    = ( (2.0*(sigma_max-sigma_0)*epsi/(1.0-sigma_0))**2) / (2.0*me*Te)
    sigma  = sigma_0 + 2.0*Te /epsi* (1.-sigma_0) + (
        sigma_max-sigma_0)*np.exp(-AR2)*(AR2+1.0) + (
        sigma_0-1.0) *Te* np.exp(-AR2)*(AR2*(AR2+2.0)+2.0)/epsi #SEE yield
    
    return sigma

def newSigma_maxw(Te, dphi,epsi,alpha):
    """Using the Non-isothermal model
    Unfortunatly, we need $\Delta \phi$ with is a function of sigma"""
    
    sigma = sigma_0 + (1 - sigma_0)/(epsi)*(2*Te - dphi/alpha)
    
    return sigma

def maxwE(etab, Te, normed = False):
    """return the Maxwellian distribution in energy"""
    
    m = 2/np.sqrt(np.pi)*np.sqrt(etab/Te)*np.exp( -0.5* etab/(Te))
    if normed:
        m /= m.max()
    return m