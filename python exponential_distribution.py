import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
mu = 2/3  # mean
nsample = 10**6  # number of random samples

# Define the grid
x = np.arange(0, 5.05, 0.05)

# Compute the PDF and the CDF
f = (1 / mu) * np.exp(-x / mu)  # PDF of Exponential Distribution
F = 1 - np.exp(-x / mu)  # CDF of Exponential Distribution

# Plot PDF and CDF
plt.figure(1)
plt.plot(x, f, 'r', label='PDF')
plt.plot(x, F, 'b', label='CDF')
plt.xlabel('x')
plt.legend(loc='best')
plt.title(r'Exponential distribution with $\mu = \frac{2}{3}$')
plt.savefig('exponential.pdf')  # Save the figure as a PDF

# Sample an exponential distribution
U = np.random.rand(nsample)  # standard uniform random numbers
X = -mu * np.log(U)  # transformation to exponential random numbers

# Bin the random variables in a histogram and normalize it
dx = x[1] - x[0]  # bin width
h, xx = np.histogram(X, bins=x + dx/2, density=True)
xx = (xx[:-1] + xx[1:]) / 2  # Take the center of the bins

# Plot sampled distribution vs theory
plt.figure(2)
plt.plot(xx, h, 'b', label='Sampled')
plt.plot(x, f, 'r', label='Theory')
plt.xlim([0, 5])
plt.xlabel('x')
plt.ylabel('f')
plt.legend(loc='best')
plt.title(r'Exponential distribution with $\mu = \frac{2}{3}$')

# Plot histogram of the sampled data
plt.figure(3)
plt.bar(xx, h, width=dx, label='Sampled', alpha=0.6)
plt.plot(x, f, 'r', label='Theory')
plt.xlabel('x')
plt.ylabel('f')
plt.legend(loc='best')
plt.title(r'Exponential distribution with $\mu = \frac{2}{3}$')

# Save all figures
plt.show()
