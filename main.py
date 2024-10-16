import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100 # 44.1Khz sample rate
sample_window = 1 # 1 second worth of samples

# generate time markers spread evenly across the time domain
t = np.arange(sample_rate*sample_window)/sample_rate 

# Generate the tone itself, one for each time marker
f = 10e3 # the frequency of the tone we are generating (10Khz; "kind of high")
x = np.sin(2*np.pi*f*t)

# Set up to do an FFT with a given slice size against the above signal
slice_size = 1024 # how many samples each FFT instance sees
num_slices = sample_rate//slice_size # how many slices we take

# Allocate space for the spectrogram data
spectrogram = np.zeros((num_slices, slice_size)) # build the spectrogram as a 2d array (starting with zeroes)

# Generate the spectrogram--each row gets the FFT for one slice.
for i in range(num_slices):
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*slice_size:(i+1)*slice_size])))**2)

# Render the spectrogram with width scaled in Khz
f_unit = 1e3 # freq shown in Khz
plt.imshow(spectrogram, aspect='auto', extent = [ sample_rate/-2/f_unit, sample_rate/2/f_unit, len(x)/sample_rate, 0])
plt.xlabel("Frequency [Khz]")
plt.ylabel("Time [s]")

plt.show()