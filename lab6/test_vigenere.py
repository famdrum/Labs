import unittest
import vigenere

class Check(unittest.TestCase):
	def test_encode_character(self):
		cipher = vigenere.VigenereCipher("TRAIN")
		encoded = cipher.encode("E")
		assert encoded == "X"
	def test_encode_spaces(self):
		cipher = vigenere.VigenereCipher("TRAIN")
		encoded = cipher.encode("ENCODED IN PYTHON")
		assert encoded == "XECWQXUIVCRKHWA"
	def test_encode_lowercase(self):
		cipher = vigenere.VigenereCipher("TRain")
		encoded = cipher.encode("encoded in Python")
		assert encoded == "XECWQXUIVCRKHWA"
	def test_combine_character(self):
		assert vigenere.combine_character("E", "T") == "X"
		assert vigenere.combine_character("N", "R") == "E"
	def test_extend_keyword(self):
		cipher = vigenere.VigenereCipher("TRAIN")
		extended = cipher.extend_keyword(16)
		assert extended == "TRAINTRAINTRAINT"
	def test_separate_character(self):
		assert vigenere.separate_character("X", "T") == "E"
		assert vigenere.separate_character("E", "R") == "N"
	def test_decode(self):
		cipher = vigenere.VigenereCipher("TRAIN")
		decoded = cipher.decode("XECWQXUIVCRKHWA")
		assert decoded == "ENCODEDINPYTHON"

if __name__ == "__main__":
	unittest.main()