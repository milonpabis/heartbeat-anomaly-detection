import numpy as np
from keras import models, layers


class AnomalyDetector:

    anomaly_q001_3 = 0.0029483

    def __init__(self, path: str, anomaly_threshold: float = anomaly_q001_3):
        self.model = models.load_model(path, custom_objects={'LeakyReLU': layers.LeakyReLU})
        self.threshold = anomaly_threshold

    
    def predict(self, signal: np.array):
        reconstructed_signal = self.model.predict(self.fix_dimension(signal))
        error = self.calculate_error(signal, reconstructed_signal)
        return (reconstructed_signal, error, (error > self.threshold).astype(int))

    
    def fix_dimension(self, signal: np.array) -> np.array:
        return np.atleast_2d(signal)


    def calculate_error(self, X_original: np.array, X_reconstructed: np.array) -> np.array:
        return np.mean(np.square(X_original - X_reconstructed), axis=1)