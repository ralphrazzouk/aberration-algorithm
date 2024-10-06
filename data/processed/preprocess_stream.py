def preprocess_stream(stream, min_freq, max_freq, taper=0.05):
    """Apply some obspy preprocessing to the stream.

    Args:
        stream (obspy.core.stream.Stream): Seismic data stream from .mseed file.
        min_freq (float): Pass band low corner frequency.
        max_freq (float): Pass band high corner frequency. (Must be less than Nyquist frequency)
        taper (float, optional): Decimal percentage of taper at one end (ranging from 0. to 0.5). Defaults to `0.05`.

    Returns:
        obspy.core.stream.Stream: Seismic data stream from .mseed file after preprocessing.
    """
    for trace in stream:
        trace.detrend(type="linear")
        trace.taper(max_percentage=taper, type="cosine")  # Adjust taper percentage
        trace.filter("bandpass", freqmin=min_freq, freqmax=max_freq)
    return stream