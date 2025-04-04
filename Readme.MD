# Qryptonite

A proof-of-concept implementation demonstrating:
1. RSA encryption
2. Breaking RSA using Shor's Algorithm
3. Post-quantum secure encryption using LWE

## Project Structure

- `rsa_implementation.py`: RSA encryption/decryption
- `shors_algorithm.py`: Simulation of Shor's Algorithm
- `lwe_implementation.py`: Learning With Errors (LWE) encryption
- `main.py`: Orchestrates all three phases

## Requirements

- Python 3.x
- numpy

## Installation

```bash
pip install numpy
```

## Usage

Run all three phases:
```bash
python main.py
```

Or run individual phases:
```bash
python rsa_implementation.py
python shors_algorithm.py
python lwe_implementation.py
```

## How It Works

1. **RSA Implementation**
   - Uses primes p=61, q=53
   - Public key (e=17, n=3233)
   - Private key (d=2753, n=3233)

2. **Shor's Algorithm**
   - Simulates quantum period finding
   - Factors n to recover p and q
   - Breaks RSA by recovering private key

3. **LWE Encryption**
   - Implements Learning With Errors
   - Quantum-resistant encryption
   - Parameters: n=10, m=20, q=97

## License

MIT License
