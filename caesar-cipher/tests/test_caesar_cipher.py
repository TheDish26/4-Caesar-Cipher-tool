import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_encryption(self):
        self.assertEqual(caesar_cipher("Hello", 3, "encrypt"), "Khoor")
        
    def test_decryption(self):
        self.assertEqual(caesar_cipher("Khoor", 3, "decrypt"), "Hello")
        
    def test_no_shift(self):
        self.assertEqual(caesar_cipher("Hello", 0, "encrypt"), "Hello")
        
    def test_non_alphabetic_characters(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3, "encrypt"), "Khoor, Zruog!")
        
if __name__ == "__main__":
    unittest.main()
