import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import butter, lfilter


def read(file_path):
    signal, samplefreq = sf.read(file_path)
    return signal, samplefreq

def HPF_filter(signal, cutoff_frequency, samplefreq):
    nyquist_freq = 0.5 * samplefreq
    b, a = butter(5, cutoff_frequency / nyquist_freq, btype='high')
    filtered_signal = lfilter(b, a, signal)
    return np.real(filtered_signal)

def time_domain_plot(signal, samplefreq, title):
    time = np.linspace(0, len(signal)*(1/samplefreq), len(signal))
    plt.figure(figsize=(13, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (seconds)")
    plt.show()

def frequency_domain_plot(signal, samplefreq, title):
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / samplefreq)
    freqs_shifted = np.fft.fftshift(freqs)
    fft_shifted = np.fft.fftshift(fft)

    absoluted = np.abs(fft_shifted)

    # Plot signal
    plt.figure(figsize=(13, 4))
    plt.plot(freqs_shifted, absoluted)
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency (Hertz)")
    plt.title(title)
    plt.show()


def save(file_path, signal, samplefreq):
    sf.write(file_path, signal, samplefreq)




signal, samplefreq = read("E:/Dove/Fall 23/Signals and Systems Fundamentals ECE251s/Project/Python Project/Voice.wav")

time_domain_plot(signal, samplefreq, "Signal in Time Domain")

frequency_domain_plot(signal, samplefreq, "Signal in Frequency Domain")

filteredsignal = HPF_filter(signal, 1000, samplefreq)
frequency_domain_plot(filteredsignal, samplefreq, "Filtered Signal in Frequency Domain")

time_domain_plot(filteredsignal, samplefreq, "Filtered Signal in Time Domain")

save("E:/Dove/Fall 23/Signals and Systems Fundamentals ECE251s/Project/Python Project/Voice_Filtered.wav", filteredsignal, samplefreq)