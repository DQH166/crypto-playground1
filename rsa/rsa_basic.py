import random
from math import gcd

# 快速幂
def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

# 生成素数（简单版，足够Demo）
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# RSA密钥生成
def generate_rsa_keys(bits=16):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3  # 选择常见的小指数
    while gcd(e, phi) != 1:
        e += 2
    # 扩展欧几里得算法求逆
    d = pow(e, -1, phi)
    return (n, e, d)

# 加解密
def encrypt(msg, n, e):
    return mod_pow(msg, e, n)

def decrypt(cipher, n, d):
    return mod_pow(cipher, d, n)

if __name__ == "__main__":
    n, e, d = generate_rsa_keys()
    print(f"[+] Public key: (n={n}, e={e})")
    print(f"[+] Private key: d={d}")

    message = 42
    cipher = encrypt(message, n, e)
    plain = decrypt(cipher, n, d)

    print(f"[+] Message: {message}")
    print(f"[+] Cipher: {cipher}")
    print(f"[+] Decrypted: {plain}")
