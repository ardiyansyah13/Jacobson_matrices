README

Project: Jacobson Radical of Matrix Rings over Z/nZ

This project provides a Python implementation to compute the Jacobson radical of the modular ring Z_n and to construct all 3x3 matrices over it.

The code is intended as both an educational tool for abstract algebra and a computational resource for exploring properties of matrix rings and radicals in number theory.

--------------------------------------------------
Features
--------------------------------------------------
- Prime factorization of integers.
- Computation of the Jacobson radical of Z_n.
- Generation of all 3x3 matrices with entries in the radical.
- Display of statistics about the ring and its radical matrices.

--------------------------------------------------
How It Works
--------------------------------------------------
1. The program asks the user to input a positive integer n.
2. It computes:
   - The number of elements in Z_n.
   - The total number of possible 3x3 matrices over Z_n.
   - The Jacobson radical of Z_n.
   - The set of all 3x3 radical matrices.
3. Results are printed to the console, including each radical matrix explicitly.

--------------------------------------------------
Example Run
--------------------------------------------------
Enter a positive integer n for Z/nZ: 12

Modulo Ring Z/12Z
========================================
• Total elements in Z/12Z: 12
• Total Matrices in M_3(Z/12Z): 5159780352
• Jacobson Radical of Z/12Z: [0, 6]
• Total Matrices in Jacobson Radical of M_3(Z/12Z): 512

All Jacobson radical matrices:
Matrix #1:
[[0 0 0]
 [0 0 0]
 [0 0 0]]

Matrix #2:
[[0 0 0]
 [0 0 0]
 [0 0 6]]
...

--------------------------------------------------
File Structure
--------------------------------------------------
- jacobson_matrices.py
  - is_prime(p) – primality test
  - prime_factors(n) – prime factorization
  - jacobson_radical_Zn(n) – compute Jacobson radical of Z_n
  - generate_jacobson_matrices(n) – generate radical matrices
  - display_matrix_info(n) – print summary and matrices

--------------------------------------------------
Requirements
--------------------------------------------------
- Python 3.x
- numpy

Install numpy if needed:
pip install numpy

--------------------------------------------------
Applications
--------------------------------------------------
- Abstract algebra education
- Research in ring theory and number theory
- Exploration of radicals of modular matrix rings
