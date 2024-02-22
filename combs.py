import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig

"""
Find the frequency response of two filters:

1. y(n) = b0 * x(n) + bM * x(n-M), where M > 1 is some integer. (If M varies with time, we get a flanger).
For b0 = b = bM, find a general formula for the number of notches and the notch frequencies as a function of M.

2. y(n) = b0 * x(n) - aM * y(n-M), 
For b0 = -aM = a, find an expression for the number of peaks and the peak frequencies as a function of M. 
How does this all-pole comb filter compare to the all-zero comb filter above? How do the peak gains compare when a=b?
(The peak gain is defined as the max. value assumed by the amplitude response G(w) over al w E [-pi, pi].)

For the all-zero filter with b0 = bM = b, the maximum gain occurs at the frequencies where the response is maximum, which is
|H(w)| = |2b|.

For the all-pole filter with b0 = -aM = a, the peak gains can theoretically go to infinity as the frequency response can approach a pole, 
but this depends on the value of a and the specific frequencies.

In comparison, the all-zero comb filter has a bounded gain, while the all-pole comb filter can have a very high or infinite peak gain, indicating a resonant 
response at the peak frequencies.

"""

M = 4
b = 1

# Create a frequency grid
omega = np.linspace(-np.pi, np.pi, 1000)

# All-zero comb filter
H_zero = b * (1 + np.exp(-1j * omega * M))

# All-pole comb filter
a = b
H_pole = a / (1 + a*np.exp(-1j * omega * M))

# Plot the frequency responses
plt.figure(figsize=(14, 6))

# All-zero comb filter magnitude response
plt.subplot(1, 2, 1)
plt.plot(omega, np.abs(H_zero))
plt.title('All-zero Comb Filter Magnitude Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid()

# All-pole comb filter magnitude response
plt.subplot(1, 2, 2)
plt.plot(omega, np.abs(H_pole))
plt.title('All-pole Comb Filter Magnitude Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid()

plt.show()
