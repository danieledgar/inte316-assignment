import numpy as np
import matplotlib.pyplot as plt

def analyze_signal(f1, f2, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(t), 1/sample_rate)
    
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_result)[:len(frequencies)//2])
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Parameters
f1, f2 = 50, 120  # Hz
sample_rate = 1000  # Hz
duration = 1  # second

analyze_signal(f1, f2, sample_rate, duration)