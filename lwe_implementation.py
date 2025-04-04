import random
import numpy as np

def generate_binary_vector(n):
    return np.array([random.randint(0, 1) for _ in range(n)])

def generate_error_vector(n, bound=2):
    return np.array([random.randint(-bound, bound) for _ in range(n)])

def lwe_keygen(n, m, q):
    A = np.array([[random.randint(0, q-1) for _ in range(n)] for _ in range(m)])
    s = generate_binary_vector(n)
    e = generate_error_vector(m)
    b = (A.dot(s) + e) % q
    return (A, b), s

def lwe_encrypt(public_key, message_bit, q):
    A, b = public_key
    m = len(b)
    r = generate_binary_vector(m)
    u = r.dot(A) % q
    v = (r.dot(b) + message_bit * (q//2)) % q
    return u, v

def lwe_decrypt(private_key, ciphertext, q):
    u, v = ciphertext
    s = private_key
    result = (v - u.dot(s)) % q
    return 1 if abs(result - q//2) < q//4 else 0

def text_to_bits(text):
    result = []
    for c in text:
        ascii_val = ord(c)
        for i in range(7, -1, -1):
            result.append((ascii_val >> i) & 1)
    return result

def bits_to_text(bits):
    result = ""
    for i in range(0, len(bits), 8):
        char_bits = bits[i:i+8]
        ascii_val = sum(b << (7-j) for j, b in enumerate(char_bits))
        result += chr(ascii_val)
    return result

def main():
    print("LWE Post-Quantum Encryption")
    print("-------------------------")
    
    n, m, q = 10, 20, 97
    print(f"LWE Parameters: n={n}, m={m}, q={q}")
    
    public_key, private_key = lwe_keygen(n, m, q)
    message = "A"
    message_bits = text_to_bits(message)
    
    ciphertexts = [lwe_encrypt(public_key, bit, q) for bit in message_bits]
    decrypted_bits = [lwe_decrypt(private_key, ct, q) for ct in ciphertexts]
    decrypted_message = bits_to_text(decrypted_bits)
    
    if decrypted_message == message:
        print("\nSuccess! LWE encryption is quantum-resistant!")
    else:
        print("\nError: LWE decryption failed")

if __name__ == "__main__":
    main() 