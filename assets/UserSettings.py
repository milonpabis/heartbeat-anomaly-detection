from assets.settings import *


class UserSettings:


    def __init__(self):
        # SIGNAL SETTINGS
        self.analyze_mode = False
        self.anomaly_threshold = DEFAULT_THRESHOLD
        self.peak_finding_threshold = DEFAULT_PEAK_THRESHOLD

        # STYLE SETTINGS
        self.sub_frame_fill_percentage = 100
        self.analyze_mode_color = (0, 0, 255)

    
    def set_analyze_mode(self, mode: bool) -> None:
        if not isinstance(mode, bool):
            raise ValueError('Analyze mode must be a boolean.')
        self.analyze_mode = mode


    def set_anomaly_threshold(self, threshold: float) -> None:
        if threshold < DEFAULT_THRESHOLD * 0.8 or threshold > DEFAULT_THRESHOLD * 1.2:
            raise ValueError('Threshold value is too extreme.')
        self.anomaly_threshold = threshold

    
    def set_peak_finding_threshold(self, threshold: float) -> None:
        if threshold < 0.6 or threshold > 0.95:
            raise ValueError('Threshold value is out of bounds. [0.6, 0.95]')
        self.peak_finding_threshold = threshold


    def set_sub_frame_fill_percentage(self, percentage: int) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError('Percentage value is out of bounds. [0, 100]')
        self.sub_frame_fill_percentage = percentage

    
    def set_analyze_mode_color(self, color: tuple) -> None:
        if not all(0 <= i <= 255 for i in color):
            raise ValueError('Color values are out of bounds. [0, 255]')
        if len(color) != 3:
            raise ValueError('Color tuple must have 3 values.')
        self.analyze_mode_color = color

