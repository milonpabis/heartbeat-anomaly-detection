import numpy as np
from keras import models, layers
from typing import Tuple


class AnomalyDetector:

    anomaly_q001_3 = 0.0029483
    normal_q090 = 0.005748231

    def __init__(self, path: str):
        self.model = models.load_model(path, custom_objects={'LeakyReLU': layers.LeakyReLU})


    
    def predict(self, signal: np.ndarray, threshold: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        reconstructed_signal = self.model.predict(self._fix_dimension(signal), verbose=0)
        error = self._calculate_error(signal, reconstructed_signal)
        return (reconstructed_signal, error, (error > threshold).astype(int))

    

    def _fix_dimension(self, signal: np.ndarray) -> np.ndarray:
        return np.atleast_2d(signal)



    def _calculate_error(self, X_original: np.ndarray, X_reconstructed: np.ndarray) -> np.ndarray:
        return np.mean(np.square(X_original - X_reconstructed), axis=1)