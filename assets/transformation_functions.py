import numpy as np
from scipy.fftpack import fft, ifft
from scipy.signal import wiener, resample


class SignalTransformer:

    def __init__(self, fs: int = 360, time_frame: float = 2.4, hz_threshold: int = 40, wiener_size: int = 9):
        self.fs = fs
        self.time_frame = time_frame
        self.hz_threshold = hz_threshold
        self.wiener_size = wiener_size

    
    def transform_signal(self, signal: np.array):
        """
        Transforms the given signal using the FFT and Wiener filter.

        Parameters
        ----------
        signal : np.array
            The signal to transform.

        Returns
        -------
        transformed_signal : np.array
            The transformed signal.
        """
        if signal.shape[0] != 864:
            signal = resample(signal, 864)

        transformed_signal = self._fft_wiener_denoise(signal)
        transformed_signal = self._normalize_signal(transformed_signal)

        return transformed_signal


    def _fft_wiener_denoise(self, signal: np.array):
        """
        Applies the FFT and Wiener filter to the given signal.
        """
        _, _, _, filtered_signal = self._fft_threshold(signal)

        return wiener(filtered_signal, mysize=self.wiener_size)
    

    def _fft_threshold(self, signal: np.array):
        """
        Cuts off the frequencies above the given threshold.

        Parameters
        ----------
        signal : np.array
            The signal to transform.

        Returns
        -------
        fft_signal : np.array
            The signal with the FFT applied.
        """
        t = np.linspace(0, self.time_frame, int(self.fs*self.time_frame))
        if self.fs == 360:
            t = t[:-1]
        
        fft_signal = fft(signal)
        frequencies = np.fft.fftfreq(len(fft_signal), 1/self.fs)

        fft_signal_filtered = fft_signal.copy()
        fft_signal_filtered[(frequencies > self.hz_threshold)] = 0

        filtered_signal = ifft(fft_signal_filtered)

        return fft_signal, fft_signal_filtered, frequencies, filtered_signal.real
    

    def _normalize_signal(self, signal: np.array):
        """
        Normalizes the signal to the range [0, 1].
        """
        min_val = np.min(signal)
        max_val = np.max(signal)

        return (signal - min_val) / (max_val - min_val)