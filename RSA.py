import random
from sympy import isprime, mod_inverse

class RSA:
    def __init__(self, primes):
        self.primes = primes
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        p = random.choice(self.primes)
        q = random.choice(self.primes)
        while p == q:
            q = random.choice(self.primes)

        n = p * q
        phi_n = (p-1) * (q-1)

        e = 65537
        d = mod_inverse(e, phi_n)

        self.public_key = (e, n)
        self.private_key = (d, n)

    def encrypt(self, message):
        e, n = self.public_key
        message_int = [ord(c) for c in message]


        cypher_int = [pow(c, e, n) for c in message_int]
        return cypher_int

    def decrypt(self, message):
        d, n = self.private_key
        decrypted_int = [pow(c, d, n) for c in message]

        return "".join(chr(c) for c in decrypted_int)

if __name__ == "__main__":
    primes_list = [i for i in range(2, 10 ** 6) if isprime(i)]

    rsa = RSA(primes_list)
    rsa.generate_keys()

    message = "Hello, world!"
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")