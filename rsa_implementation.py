import math
import random
from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = extended_gcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def text_to_int(text):
    result = 0
    for char in text:
        result = result * 256 + ord(char)
    return result

def int_to_text(n):
    result = ""
    while n > 0:
        result = chr(n % 256) + result
        n = n // 256
    return result

def rsa_encrypt(message, e, n):
    m = text_to_int(message)
    if m >= n:
        raise ValueError("Message too large for the given key size")
    return pow(m, e, n)

def rsa_decrypt(ciphertext, d, n):
    m = pow(ciphertext, d, n)
    return int_to_text(m)

def main():
    print("RSA Implementation")
    print("-----------------")
    
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = modinv(e, phi)
    
    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")
    
    message = "A"
    print(f"\nOriginal message: {message}")
    
    try:
        ciphertext = rsa_encrypt(message, e, n)
        print(f"Encrypted (decimal): {ciphertext}")
        
        decrypted = rsa_decrypt(ciphertext, d, n)
        print(f"Decrypted message: {decrypted}")
        
        if decrypted == message:
            print("\nSuccess! RSA encryption/decryption worked.")
            
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 