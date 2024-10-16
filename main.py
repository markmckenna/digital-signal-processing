import numpy as np

t = np.arange(100) # array containing numbers from [0..99] (think of them as seconds)
s = np.sin(0.15*2*np.pi*t) # array containing 100 samples of a sine wave at 0.15hz, one per second
S = np.fft.fft(s) # fourier space transform of s: 100 elements showing 

import matplotlib.pyplot as plt