import random
from math import gcd
from rsa_implementation import rsa_decrypt, modinv

def find_period(a, n):
    x = a
    r = 1
    while x != 1:
        x = (x * a) % n
        r += 1
        if r > n:
            return None
    return r

def shor_factor(n):
    if n % 2 == 0:
        return 2, n//2
    
    while True:
        a = random.randint(2, n-1)
        if gcd(a, n) != 1:
            factor = gcd(a, n)
            return factor, n//factor
        
        r = find_period(a, n)
        if r is None or r % 2 != 0:
            continue
            
        x = pow(a, r//2, n)
        if x == n-1:
            continue
            
        p = gcd(x+1, n)
        q = gcd(x-1, n)
        if p * q == n:
            return p, q

def main():
    print("Shor's Algorithm Simulation")
    print("-------------------------")
    
    # RSA parameters
    p, q = 61, 53
    n = p * q
    e = 17
    
    # Encrypted message from RSA
    ciphertext = 2790
    message = "A"
    
    print(f"Attempting to factor n = {n}")
    
    recovered_p, recovered_q = shor_factor(n)
    print(f"Recovered factors: p = {recovered_p}, q = {recovered_q}")
    
    if recovered_p * recovered_q == n:
        recovered_phi = (recovered_p - 1) * (recovered_q - 1)
        recovered_d = modinv(e, recovered_phi)
        recovered_message = rsa_decrypt(ciphertext, recovered_d, n)
        
        if recovered_message == message:
            print("Successfully broke RSA!")
        else:
            print("Failed to decrypt with recovered key")
    else:
        print("Failed to factor n correctly")

if __name__ == "__main__":
    main() 