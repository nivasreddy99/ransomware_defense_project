import unittest
import os
import tempfile
from src.encryption_tool import EncryptionTool

class TestEncryptionTool(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.key_file = os.path.join(self.temp_dir, 'test_key.key')
        self.encryption_tool = EncryptionTool(self.key_file)

    def tearDown(self):
        os.remove(self.key_file)
        os.rmdir(self.temp_dir)

    def test_encrypt_decrypt_file(self):
        test_file = os.path.join(self.temp_dir, 'test_file.txt')
        original_content = b"This is a test file."
        
        # Write test file
        with open(test_file, 'wb') as f:
            f.write(original_content)
        
        # Encrypt the file
        self.encryption_tool.encrypt_file(test_file)
        
        # Check that the file content has changed
        with open(test_file, 'rb') as f:
            encrypted_content = f.read()
        self.assertNotEqual(original_content, encrypted_content)
        
        # Decrypt the file
        self.encryption_tool.decrypt_file(test_file)
        
        # Check that the file content is restored
        with open(test_file, 'rb') as f:
            decrypted_content = f.read()
        self.assertEqual(original_content, decrypted_content)

if __name__ == '__main__':
    unittest.main()