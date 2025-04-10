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

import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_encryption(self):
        # Test case for encryption with a shift of 3
        self.assertEqual(caesar_cipher("Hello World", 3, "encrypt"), "Khoor Zruog")

    def test_decryption(self):
        # Test case for decryption with a shift of 3
        self.assertEqual(caesar_cipher("Khoor Zruog", 3, "decrypt"), "Hello World")

    def test_no_shift(self):
        # Test case where no shift should happen
        self.assertEqual(caesar_cipher("Hello World", 0, "encrypt"), "Hello World")
        
    def test_non_alphabetic_characters(self):
        # Test case with non-alphabetic characters (should not be shifted)
        self.assertEqual(caesar_cipher("Hello, World!", 3, "encrypt"), "Khoor, Zruog!")
        
if __name__ == "__main__":
    unittest.main()
# End of code snippet