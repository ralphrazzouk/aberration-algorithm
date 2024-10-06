import numpy as np
import matplotlib.pyplot as plt

def plot_fft(trace):
    """Plot a graph of the Discrete Fourier Transform of the seismic data.

    Args:
        trace (obspy.core.stream.Stream): Seismic data stream from .mseed file.
    """
    npts = trace.stats.npts
    sampling_rate = trace.stats.sampling_rate
    freqs = np.fft.fftfreq(npts, d=1 / sampling_rate)
    fft_values = np.fft.fft(trace.data)

    plt.plot(np.abs(freqs), np.abs(fft_values))
    plt.title("FFT of the Seismic Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 0.005)  # Limit to your Nyquist frequency
    plt.show()