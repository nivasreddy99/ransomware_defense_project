import unittest
import os
import tempfile
from src.mitigation_engine import MitigationEngine

class TestMitigationEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        config = {
            'QuarantineDir': os.path.join(self.temp_dir, 'quarantine')
        }
        self.mitigation_engine = MitigationEngine(config)

    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def test_quarantine_file(self):
        test_file = os.path.join(self.temp_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write("This is a test file.")
        
        self.mitigation_engine.quarantine_file(test_file)
        
        self.assertFalse(os.path.exists(test_file))
        self.assertTrue(os.path.exists(os.path.join(self.mitigation_engine.quarantine_dir, 'test_file.txt')))

if __name__ == '__main__':
    unittest.main()