# https://chem.libretexts.org/Ancillary_Materials/Interactive_Applications/Jupyter_Notebooks/Quantum_Harmonic_Oscillators_-_Plotting_Eigenstates_(Python_Notebook)
import matplotlib
import matplotlib.pyplot as plt 
import numpy
import numpy.polynomial.hermite as Herm

#Choose simple units
m=1.
w=1.
hbar=1.

#Discretized space
dx = 0.05
x_lim = 12
x = numpy.arange(-x_lim,x_lim,dx)

def hermite(x, n):
    xi = numpy.sqrt(m*w/hbar)*x
    herm_coeffs = numpy.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
  
plt.figure()
plt.plot(x, hermite(x,0), linewidth=2, label=r"$H_0$")
plt.plot(x, hermite(x,1), linewidth=2, label=r"$H_1$")
plt.plot(x, hermite(x,2), linewidth=2, label=r"$H_2$")
plt.plot(x, hermite(x,3), linewidth=2, label=r"$H_3$")
plt.plot(x, hermite(x,4), linewidth=2, label=r"$H_4$")

#Set limits for axes
plt.xlim([-2.5,2.5])
plt.ylim([-20,20])

#Set axes labels
plt.xlabel("x")
plt.ylabel(r"$H_n(\xi)$")
plt.title(r"Hermite Polynomials, $H_n(\xi)$")
plt.legend()
# plt.show()
plt.savefig("output/hermite_polynomials.png")
