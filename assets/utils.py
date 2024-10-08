import numpy as np
from typing import Tuple
import wfdb
import cv2

from assets.transformation_functions import SignalTransformer
from assets.settings import *


COLORS = {"White": (255, 255, 255), 
          "Red": (255, 0, 0), 
          "Green": (0, 255, 0), 
          "Blue": (0, 0, 255), 
          "Yellow": (255, 255, 0), 
          "Cyan": (0, 255, 255), 
          "Magenta": (255, 0, 255)}


def load_full_ecg(path: str, id: str) -> Tuple[np.ndarray, np.ndarray, list]:
    """
    Loads the full ECG signal with the annotation from the given path and id.
    """
    record = wfdb.rdrecord(path + id)
    ann = wfdb.rdann(path + id, "atr")

    signal = record.p_signal[:, 0] # MLII
    ann_sample = ann.sample # annotation locations
    ann_symbol = ann.symbol # annotation symbols
    
    return signal, ann_sample, ann_symbol



def load_signal_ecg(path: str) -> np.ndarray:
    """
    Loads the ECG signal from the given path.
    """
    record = wfdb.rdrecord(path)
    return record.p_signal[:, 0] # not dat but hea and without the extension



def convert_signal_to_image(signal: np.ndarray, peak_idx: int, h: int, w: int, color: tuple = (0, 255, 0)) -> np.ndarray:
    """
    Converts the given signal to an image.
    """

    transformer = SignalTransformer()

    transformed_signal = transformer.transform_signal(np.hstack([signal[peak_idx-432:peak_idx], signal[peak_idx:peak_idx+432]]))

    black_image = np.ones((h, 864, 3), dtype=np.uint8) * 0

    for i in range(1, len(transformed_signal)):
        cv2.line(black_image, (i-1, int(h - h * transformed_signal[i-1])), (i, int(h - h * transformed_signal[i])), color, 1)

    return cv2.resize(black_image, (w, h), interpolation=cv2.INTER_LINEAR)



def map_to_rgb(value) -> Tuple[int, int, int]: # primitive version
    # normalization
    t = value / 0.015
    
    if t <= 0.5:
        # interpolation between green (0, 255, 0) and orange (255, 165, 0)
        r = int(2 * t * 255)
        g = int(255 - (90 * 2 * t))
        b = 0
    else:
        # interpolation between orange (255, 165, 0) and red (255, 0, 0)
        t = (t - 0.5) * 2  # normalization
        r = 255
        g = int(165 - (165 * t))
        b = 0
    
    return (r, g, b)
