import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig

"""
Derive the frequency response for the two digital filters:
1. y(n) = x(n-1) + x(n-2) + y(n-1)
2. y(n) = x(n) + x(n-1) + y(n-1)

Plot the magnitude and phase response for each filter.
In what way are these filters identical? How are they different?

"""

# Define the transfer function for each filter
Num = [0, 1, 1] # Reflecting x(n-1) + x(n-2)
Den = [1, -1] # Reflecting 1 - y(n-1)

Num2 = [1, 1]
Den2 = [1, -1]

H_z1 = sig.TransferFunction(Num, Den, dt=1)
H_z2 = sig.TransferFunction(Num2, Den2, dt=1)
w, mag, phase = sig.dbode(H_z1, n=512)
w2, mag2, phase2 = sig.dbode(H_z2, n=512)

# plot the magnitude and phase response
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, mag, label='Filter 1')
plt.plot(w2, mag2, label='Filter 2')
plt.title('Magnitude Response')
plt.ylabel('Magnitude [dB]')
plt.xlabel('Frequency [rad/sample]')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


