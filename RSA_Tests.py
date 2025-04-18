import unittest
from sympy import isprime
from RSA import RSA

class RSA_Tests(unittest.TestCase):
    def setUp(self):
        self.primes_list = [i for i in range(2, 10 ** 6) if isprime(i)]
        self.rsa = RSA(self.primes_list)

    def test_key_generation(self):
        self.rsa.generate_keys()
        self.assertIsNotNone(self.rsa.public_key)
        self.assertIsNotNone(self.rsa.private_key)

    def test_encryption_decryption(self):
        self.rsa.generate_keys()

        message = "Test message"

        encrypted_message = self.rsa.encrypt(message)

        decrypted_message = self.rsa.decrypt(encrypted_message)

        self.assertEqual(message, decrypted_message)

    def test_empty_string(self):
        self.rsa.generate_keys()
        string = self.rsa.encrypt("")
        self.assertEqual(self.rsa.decrypt(string), "")

    def test_special_characters(self):
        self.rsa.generate_keys()
        message = self.rsa.encrypt("!@$%^")
        self.assertEqual(self.rsa.decrypt(message), "!@$%^")

if __name__ == "__main__":
    unittest.main()