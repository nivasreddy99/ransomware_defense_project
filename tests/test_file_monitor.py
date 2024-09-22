import unittest
from unittest.mock import Mock, patch
from src.file_monitor import FileMonitor

class TestFileMonitor(unittest.TestCase):
    def setUp(self):
        self.mock_detection_engine = Mock()
        self.file_monitor = FileMonitor(self.mock_detection_engine)

    def test_on_modified(self):
        mock_event = Mock()
        mock_event.is_directory = False
        mock_event.src_path = '/test/file.txt'

        with patch('logging.info') as mock_log:
            self.file_monitor.on_modified(mock_event)

        mock_log.assert_called_once_with("File modified: /test/file.txt")
        self.mock_detection_engine.analyze_event.assert_called_once_with('/test/file.txt')

    def test_on_modified_directory(self):
        mock_event = Mock()
        mock_event.is_directory = True
        mock_event.src_path = '/test/dir'

        self.file_monitor.on_modified(mock_event)

        self.mock_detection_engine.analyze_event.assert_not_called()

if __name__ == '__main__':
    unittest.main()