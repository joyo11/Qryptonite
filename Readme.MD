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

## Technologies Used

- **Python**: Core programming language
- **NumPy**: Scientific computing for matrix operations
- **RSA**: Classical public-key cryptosystem
- **Shor's Algorithm**: Quantum factoring algorithm (simulated)
- **LWE**: Learning With Errors post-quantum cryptography
- **Modular Arithmetic**: Core mathematical operations
- **Extended Euclidean Algorithm**: For modular inverses

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

## Why LWE is Quantum-Resistant

LWE (Learning With Errors) is considered quantum-resistant for several fundamental reasons:

1. **Noise-Based Security**
   - Unlike RSA which relies on clean mathematical problems (factoring)
   - LWE introduces intentional noise/errors in the encryption process
   - This noise disrupts quantum superposition and interference patterns

2. **Mathematical Hardness**
   - The core problem reduces to finding short vectors in high-dimensional lattices
   - Even quantum computers cannot efficiently solve this problem
   - Best known quantum algorithms still require exponential time

3. **Error Amplification**
   - Small errors in the initial setup get amplified through matrix operations
   - Quantum computers cannot "clean up" these errors efficiently
   - The noise makes quantum speedup ineffective

4. **Multiple Security Layers**
   - Combines matrix operations with modular arithmetic
   - Adds random error terms at multiple stages
   - Creates a complex web of interdependent operations

5. **NIST Standardization**
   - Selected by NIST as a post-quantum cryptography standard
   - Has withstood extensive cryptanalysis from both classical and quantum perspectives
   - Considered secure against all known quantum algorithms

## Future Enhancements

- Larger key size support
- Parallel processing for faster computations
- GUI interface for visualization
- Support for longer messages
- Real quantum computer integration
- Additional post-quantum algorithms
- Performance benchmarking tools
- Security analysis tools

## Contact

For questions or support:
- Email: shafay11august@gmail.com
- GitHub: [@joyo11](https://github.com/joyo11)

## License

Copyright (c) 2025 Mohammad Shafay Joyo

MIT License
