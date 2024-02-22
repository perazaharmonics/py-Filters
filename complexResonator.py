import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig
from scipy.signal import dlti

"""
Implement a complex resonator with a transfer function of the form
H(e^jwT) = 1 / (1 - (R * e^j*theta) * e^-jwT)
where R is the magnitude of the pole and theta is the phase of the pole.
"""
# Resonator parameters
R = 0.99
theta = np.pi / 4
T = 1

# Frequency response
w = np.linspace(-np.pi, np.pi, 1000)
H = 1 / (1 - (R * np.exp(1j * theta)) * np.exp(-1j * w * T))
# Create a discrete-time system
system = dlti([1], [T, 1])

# Plot frequency response
plt.plot(w, np.abs(H))
plt.title('Frequency response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.show()

# Impulse response
n = np.arange(0, 100)
h = R**n * np.cos(theta * n)

# Plot impulse response
plt.stem(n, h)
plt.title('Impulse response')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()


