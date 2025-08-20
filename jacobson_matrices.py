import itertools
import numpy as np

def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def prime_factors(n):
    """Return a list of (p, k) where p is prime and p^k divides n."""
    factors = []
    for p in range(2, n+1):
        if is_prime(p):
            k = 0
            m = n
            while m % p == 0:
                m //= p
                k += 1
            if k > 0:
                factors.append((p, k))
    return factors

def jacobson_radical_Zn(n):
    """
    Returns the Jacobson radical of Z_n as a list of elements.
    If n = p^k and k > 1, the radical is pZ_n.
    If n is semisimple (square-free), radical is {0}.
    """
    factors = prime_factors(n)
    J = set()
    for p, k in factors:
        if k > 1:
            J.update({(i * p) % n for i in range(n // p)})
    if not J:
        J = {0}
    return sorted(J)

def generate_jacobson_matrices(n):
    """
    Generate all 3x3 matrices over Z_n with entries in the Jacobson radical of Z_n.
    """
    JZ = jacobson_radical_Zn(n)
    matrices = []
    for entries in itertools.product(JZ, repeat=9):
        matrix = np.array(entries).reshape((3, 3))
        matrices.append(matrix)
    return JZ, matrices

def display_matrix_info(n):
    """
    Display information about the Jacobson radical of Z_n and its corresponding 3x3 matrices.
    """
    print(f"\nModulo Ring Z/{n}Z")
    print("=" * 40)

    # Total elements in Z_n
    total_elements_Zn = n
    # Total matrices in M_3(Z_n)
    total_matrices_M3Zn = total_elements_Zn ** (3 * 3)
    print(f"• Total elements in Z/{n}Z: {total_elements_Zn}")
    print(f"• Total Matrices in M_3(Z/{n}Z): {total_matrices_M3Zn}")

    JZ, radical_matrices = generate_jacobson_matrices(n)
    print(f"• Jacobson Radical of Z/{n}Z: {JZ}")
    print(f"• Total Matrices in Jacobson Radical of M_3(Z/{n}Z): {len(radical_matrices)}")

    print("\nAll Jacobson radical matrices:")
    for idx, mat in enumerate(radical_matrices, 1):
        print(f"\nMatrix #{idx}:\n{mat}")

# --- Execution block ---

try:
    n_input = int(input("Enter a positive integer n for Z/nZ: "))
    if n_input <= 0:
        print("n must be a positive integer.")
    else:
        display_matrix_info(n_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
