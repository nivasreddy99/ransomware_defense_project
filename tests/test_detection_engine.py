import unittest
import time
from src.detection_engine import DetectionEngine

class TestDetectionEngine(unittest.TestCase):
    def setUp(self):
        config = {
            'EventWindowSize': '5',
            'EventThreshold': '3',
            'TimeWindowSeconds': '10'
        }
        self.detection_engine = DetectionEngine(config)

    def test_analyze_event_below_threshold(self):
        for i in range(2):
            self.detection_engine.analyze_event(f'/test/file{i}.txt')
        
        self.assertEqual(len(self.detection_engine.event_window), 2)

    def test_analyze_event_above_threshold(self):
        with self.assertLogs(level='WARNING') as cm:
            for i in range(4):
                self.detection_engine.analyze_event(f'/test/file{i}.txt')
        
        self.assertEqual(len(self.detection_engine.event_window), 4)
        self.assertIn('WARNING:root:Potential ransomware activity detected!', cm.output[0])

    def test_time_window(self):
        for i in range(3):
            self.detection_engine.analyze_event(f'/test/file{i}.txt')
        
        time.sleep(11)  # Wait for time window to pass
        self.detection_engine.analyze_event('/test/file3.txt')
        
        self.assertEqual(len(self.detection_engine.event_window), 1)

if __name__ == '__main__':
    unittest.main()