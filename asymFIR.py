import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig

"""
Asymmetric FIR Filter: Consider the impulse response 
h(n) = [1, -1]
a) Determine the frequency response H(e^jw) of the filter.
b) Determine the phase delay of the filter.
c) Determine the group delay of the filter.
"""
# Define the impulse response
h = np.array([1, -1])
# a) Determine the frequency response H(e^jw) of the filter.
w, H = sig.freqz(h)


# b) Determine the phase delay of the filter.
phase = np.unwrap(np.angle(H))
phase_delay = -phase / w
# Fix division by zero for phase delay at w=0
phase_delay[0] = phase_delay[1]

# c) Determine the group delay of the filter.
w_gd, group_delay = sig.group_delay((h, 1))
group_delay = np.array(group_delay)


# Plotting Frequency Response

plt.subplot(3, 1, 1)
plt.plot(w, abs(H))
plt.title('Frequency Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')

# Plotting Phase Delay
plt.subplot(3, 1, 2)
plt.plot(w, phase_delay)
plt.title('Phase Delay')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase Delay (samples)')

# Plotting Group Delay
plt.subplot(3, 1, 3)
plt.plot(w_gd, group_delay)
plt.title('Group Delay')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Group Delay (samples)')


plt.tight_layout()
plt.show()
