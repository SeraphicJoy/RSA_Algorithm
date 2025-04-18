# README
## RSA Algorithm
This program allows you to encrypt messages using the RSA algorithm:
1. Choose two large prime numbers p and q.
2. Compute n = pq.
3. Compute φ(n) (phi of n is used in the original paper of RSA instead of lambda).
4. Most common integer e for RSA is 65537 (1<e<φ(n))
5. d is the modular multiplicative inverse of e mod φ(n) (e**(−1)%φ(n))
6. Public key consists of exponent e and modulus n.
7. Private key consists of exponent d and modulus n.
8. The message is transformed into integer string m.
9. The encrypted cipher is calculated as m**e%n.
10. The decrypted cipher is calculated as encrypted cipher m2**d%n
11. The result is then transformed back into text string.

## Installation
1. Make sure to have Python version 3.X installed.
2. Download the code from repository onto your computer.

## Launch
1. Open a terminal or a command prompt.
2. Open folder with the code.
3. Launch program with the following code:
`python RSA.py`

## Testing
1. Open a terminal or a command prompt.
2. Open folder with the code.
3. Launch the program with the following code: 
`python -m unittest RSA_Tests.py`