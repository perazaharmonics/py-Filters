import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig

"""
A Zero-Phase is a special case of a linear-phase filter, in which the phase slope is 0. The real impulse response
h(n) of a zero-phase filter is symmetric (even), i.e., h(n) = h(-n) [Zero-Phase condition]. 
Verify this by showing the impulse response:
h(n) = 0.5 * (delta(n+1) + delta(n-1)) + 0.43*delta(n)

"""

# Define the filter coefficients
h = [0.7 , 0.43, 0.7] # h(n) = 0.5 * (delta(n+1) + delta(n-1)) + 0.43*delta(n)

# Plot the impulse response
# Plot the impulse response
plt.stem(h)
plt.title('Impulse Response')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.show()

# Compute the frequency response of the filter
w, H = sig.freqz(h) 

# Unwrap the phase of the frequency response
phi = np.unwrap(np.angle(H))

# Plot the bode plot
plt.figure()
plt.subplot(2,1,1)
plt.plot(w, 20*np.log10(abs(H)))
plt.title('Magnitude Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.subplot(2,1,2)
plt.plot(w, phi)
plt.title('Phase Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid()
plt.show()

