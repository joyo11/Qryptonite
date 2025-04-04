import math
import random
from fractions import Fraction
from math import gcd
import numpy as np
from rsa_implementation import rsa_encrypt, rsa_decrypt, modinv
from shors_algorithm import shor_factor
from lwe_implementation import lwe_keygen, lwe_encrypt, lwe_decrypt, text_to_bits, bits_to_text

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find gcd and coefficients
    Returns (gcd, x, y) where ax + by = gcd(a, b)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """
    Find modular inverse using Extended Euclidean Algorithm
    Returns x where (a * x) % m == 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def text_to_int(text):
    """Convert text to integer using ASCII values"""
    result = 0
    for char in text:
        result = result * 256 + ord(char)
    return result

def int_to_text(n):
    """Convert integer back to text"""
    result = ""
    while n > 0:
        result = chr(n % 256) + result
        n = n // 256
    return result

def find_period(a, n):
    """
    Simulate quantum period finding for Shor's algorithm
    Returns the period r where a^r ≡ 1 (mod n)
    """
    # In a real quantum computer, this would use quantum Fourier transform
    # Here we just directly compute the period classically
    x = a
    r = 1
    while x != 1:
        x = (x * a) % n
        r += 1
        if r > n:  # Safeguard against infinite loop
            return None
    return r

def generate_binary_vector(n):
    """Generate a random binary vector of length n"""
    return np.array([random.randint(0, 1) for _ in range(n)])

def generate_error_vector(n, bound=2):
    """Generate error vector with small random values"""
    return np.array([random.randint(-bound, bound) for _ in range(n)])

def main():
    # Phase 1: RSA Implementation
    print("Phase 1: Manual RSA Implementation")
    print("----------------------------------")
    
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = modinv(e, phi)
    
    message = "A"
    print(f"Original message: {message}")
    
    try:
        ciphertext = rsa_encrypt(message, e, n)
        print(f"Encrypted (decimal): {ciphertext}")
        
        decrypted = rsa_decrypt(ciphertext, d, n)
        print(f"Decrypted message: {decrypted}")
        
        if decrypted == message:
            print("Success! RSA encryption/decryption worked.")
            
        # Phase 2: Breaking RSA
        print("\nPhase 2: Breaking RSA using Shor's Algorithm")
        print("-------------------------------------------")
        
        recovered_p, recovered_q = shor_factor(n)
        print(f"Recovered factors: p = {recovered_p}, q = {recovered_q}")
        
        if recovered_p * recovered_q == n:
            recovered_phi = (recovered_p - 1) * (recovered_q - 1)
            recovered_d = modinv(e, recovered_phi)
            recovered_message = rsa_decrypt(ciphertext, recovered_d, n)
            
            if recovered_message == message:
                print("Successfully broke RSA!")
        
        # Phase 3: LWE Encryption
        print("\nPhase 3: Post-Quantum LWE Encryption")
        print("-------------------------------------")
        
        n, m, q = 10, 20, 97
        print(f"LWE Parameters: n={n}, m={m}, q={q}")
        
        public_key, private_key = lwe_keygen(n, m, q)
        message_bits = text_to_bits(message)
        
        ciphertexts = [lwe_encrypt(public_key, bit, q) for bit in message_bits]
        decrypted_bits = [lwe_decrypt(private_key, ct, q) for ct in ciphertexts]
        decrypted_message = bits_to_text(decrypted_bits)
        
        if decrypted_message == message:
            print("\nSuccess! LWE encryption is quantum-resistant!")
            
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 