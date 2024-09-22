from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

class FileMonitor(FileSystemEventHandler):
    """Monitors file system events and triggers the detection engine."""

    def __init__(self, detection_engine):
        """
        Initialize the FileMonitor.

        Args:
            detection_engine (DetectionEngine): Instance of the detection engine.
        """
        self.detection_engine = detection_engine

    def on_modified(self, event):
        """
        Called when a file is modified.

        Args:
            event (FileSystemEvent): The event object representing the file system event.
        """
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")
            self.detection_engine.analyze_event(event.src_path)

def setup_monitoring(critical_dir, detection_engine):
    """
    Set up file system monitoring for the critical directory.

    Args:
        critical_dir (str): Path to the directory to be monitored.
        detection_engine (DetectionEngine): Instance of the detection engine.

    Returns:
        Observer: The file system observer object.
    """
    event_handler = FileMonitor(detection_engine)
    observer = Observer()
    observer.schedule(event_handler, critical_dir, recursive=True)
    observer.start()
    return observer