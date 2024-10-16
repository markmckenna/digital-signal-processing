import numpy as np

t = np.arange(100) # array containing numbers from [0..99] (think of them as seconds)
s = np.sin(0.15*2*np.pi*t) # array containing 100 samples of a sine wave at 0.15hz, one per second
S = np.fft.fft(s) # frequency domain (Fourier space) representation of s

import matplotlib.pyplot as plt
S_mag = np.abs(S) # array of magnitudes of Fourier signals
S_phase = np.angle(S) # array of phases of Fourier signals
plt.plot(t, S_mag, '.-')
plt.plot(t, S_phase, '.-')

plt.show()