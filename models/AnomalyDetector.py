import numpy as np
from keras import models, layers
from typing import Tuple


class AnomalyDetector:

    anomaly_q001_3 = 0.0029483
    normal_q090 = 0.005748231

    def __init__(self, path: str, anomaly_threshold: float = normal_q090):
        self.model = models.load_model(path, custom_objects={'LeakyReLU': layers.LeakyReLU})
        self.threshold = anomaly_threshold

    
    def predict(self, signal: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        reconstructed_signal = self.model.predict(self.fix_dimension(signal))
        error = self.calculate_error(signal, reconstructed_signal)
        return (reconstructed_signal, error, (error > self.threshold).astype(int))

    
    def fix_dimension(self, signal: np.ndarray) -> np.ndarray:
        return np.atleast_2d(signal)


    def calculate_error(self, X_original: np.ndarray, X_reconstructed: np.ndarray) -> np.ndarray:
        return np.mean(np.square(X_original - X_reconstructed), axis=1)