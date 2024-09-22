import os
from cryptography.fernet import Fernet

class EncryptionTool:
    """Handles file encryption and decryption operations."""

    def __init__(self, key_file):
        """
        Initialize the EncryptionTool.

        Args:
            key_file (str): Path to the file containing the encryption key.
        """
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                self.key = file.read()
        else:
            self.key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(self.key)
        self.fernet = Fernet(self.key)

    def encrypt_file(self, file_path):
        """
        Encrypt a file.

        Args:
            file_path (str): Path to the file to be encrypted.
        """
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.fernet.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        """
        Decrypt a file.

        Args:
            file_path (str): Path to the file to be decrypted.
        """
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)