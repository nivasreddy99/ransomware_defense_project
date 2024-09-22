import os
import time
import logging
import configparser
from src.encryption_tool import EncryptionTool
from src.file_monitor import setup_monitoring
from src.detection_engine import DetectionEngine
from src.mitigation_engine import MitigationEngine

# Set up logging
logging.basicConfig(filename='logs/ransomware_defense.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def load_config():
    """Load configuration from config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def main():
    """Main function to set up and run the ransomware defense system."""
    # Load configuration
    config = load_config()
    critical_dir = config['Directories']['CriticalDir']
    key_file = config['Encryption']['KeyFile']

    # Initialize components
    encryption_tool = EncryptionTool(key_file)
    detection_engine = DetectionEngine(config['Detection'])
    mitigation_engine = MitigationEngine(config['Mitigation'])

    # Set up file monitoring
    observer = setup_monitoring(critical_dir, detection_engine)

    logging.info("Ransomware defense system started.")
    print("Ransomware defense system is running. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Ransomware defense system stopped by user.")
    observer.join()

if __name__ == "__main__":
    main()