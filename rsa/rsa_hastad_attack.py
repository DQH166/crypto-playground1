from math import isqrt
from rsa_basic import encrypt, generate_rsa_keys

# 小e广播攻击（Håstad）
# 条件：相同明文M，用相同e加密到不同模数n1, n2, n3...
# 如果e=3，可以通过CRT恢复M^e再开e次方得到M

def chinese_remainder_theorem(ciphers, moduli):
    """Solve x ≡ c_i (mod n_i) using CRT"""
    N = 1
    for n in moduli:
        N *= n
    result = 0
    for c, n in zip(ciphers, moduli):
        Ni = N // n
        inv = pow(Ni, -1, n)
        result += c * Ni * inv
    return result % N, N

def integer_nth_root(x, n):
    """Return floor(x ** (1/n))"""
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid**n < x:
            low = mid + 1
        elif mid**n > x:
            high = mid - 1
        else:
            return mid
    return high  # closest integer root

if __name__ == "__main__":
    message = 42
    e = 3
    keys = [generate_rsa_keys(16) for _ in range(3)]
    ciphers = []
    moduli = []

    for (n, _, d) in keys:
        c = encrypt(message, n, e)
        ciphers.append(c)
        moduli.append(n)

    combined, N = chinese_remainder_theorem(ciphers, moduli)
    recovered = integer_nth_root(combined, e)

    print(f"[+] Real message: {message}")
    print(f"[+] Recovered by attack: {recovered}")
