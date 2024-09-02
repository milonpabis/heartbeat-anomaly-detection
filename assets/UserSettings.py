from assets.settings import *


class UserSettings:


    def __init__(self):
        # SIGNAL SETTINGS
        self.analyze_mode = False
        self.anomaly_threshold = DEFAULT_THRESHOLD
        self.analyze_window_length = FRAME_SIZE // 2
        self.peak_finding_threshold = 0.8

        # STYLE SETTINGS
        self.sub_frame_fill_percentage = 100
        self.analyze_mode_color = (255, 0, 0)

    
    def set_analyze_mode(self, mode: bool) -> None:
        self.analyze_mode = mode


    def set_anomaly_threshold(self, threshold: float) -> None:
        if threshold < DEFAULT_THRESHOLD * 0.8 or threshold > DEFAULT_THRESHOLD * 1.2:
            raise ValueError('Threshold value is too extreme.')
        self.anomaly_threshold = threshold

    
    def set_analyze_window_length(self, length: int) -> None:
        self.analyze_window_length = length

    
    def set_peak_finding_threshold(self, threshold: float) -> None:
        self.peak_finding_threshold = threshold


    def set_sub_frame_fill_percentage(self, percentage: int) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError('Percentage value is out of bounds.')
        self.sub_frame_fill_percentage = percentage

    
    def set_analyze_mode_color(self, color: tuple) -> None:
        self.analyze_mode_color = color

