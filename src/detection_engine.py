import time
import logging
from collections import deque

class DetectionEngine:
    """Analyzes file system events to detect potential ransomware activity."""

    def __init__(self, config):
        """
        Initialize the DetectionEngine.

        Args:
            config (ConfigParser): Configuration object containing detection settings.
        """
        self.event_window = deque(maxlen=int(config['EventWindowSize']))
        self.threshold = int(config['EventThreshold'])
        self.time_window = int(config['TimeWindowSeconds'])

    def analyze_event(self, file_path):
        """
        Analyze a file system event for potential ransomware activity.

        Args:
            file_path (str): Path to the file that triggered the event.
        """
        current_time = time.time()
        self.event_window.append((current_time, file_path))

        # Remove events outside the time window
        while self.event_window and current_time - self.event_window[0][0] > self.time_window:
            self.event_window.popleft()

        if len(self.event_window) > self.threshold:
            self.trigger_alert(file_path)

    def trigger_alert(self, file_path):
        """
        Trigger an alert for potential ransomware activity.

        Args:
            file_path (str): Path to the file that triggered the alert.
        """
        message = f"Potential ransomware activity detected! File: {file_path}"
        logging.warning(message)
        # Here you would implement your alert mechanism (e.g., email, SMS)
        print(f"ALERT: {message}")