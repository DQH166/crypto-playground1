from Crypto.Util.number import long_to_bytes
import math

# 题目给定的 public values
q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

# 1) 定义格基 b1=(h,1), b2=(q,0) 并做 Gauss 二维约减（找短向量）
def norm2(v):
    return v[0]*v[0] + v[1]*v[1]

def gauss_reduce(b1, b2):
    # b1, b2 are lists [x,y]
    B1 = b1[:]
    B2 = b2[:]
    while True:
        # 保证 B1 的长度 <= B2 的长度
        if norm2(B2) < norm2(B1):
            B1, B2 = B2, B1
        # mu = round((B1·B2) / |B1|^2)
        num = B1[0]*B2[0] + B1[1]*B2[1]
        den = norm2(B1)
        # 四舍五入整数
        mu = (num + den//2) // den
        if mu == 0:
            return B1, B2
        # B2 = B2 - mu * B1
        B2 = [B2[0] - mu*B1[0], B2[1] - mu*B1[1]]

b1 = [h, 1]
b2 = [q, 0]
v_short, v_other = gauss_reduce(b1, b2)

# v_short 通常等于 (g, f) 或者带负号的 (±g, ±f)
cand_g = abs(v_short[0])
cand_f = abs(v_short[1])

print("候选 f (bitlen):", cand_f.bit_length())
print("候选 g (bitlen):", cand_g.bit_length())

# 2) 验证 h == inverse(f, q) * g mod q
f_inv_mod_q = pow(cand_f, -1, q)
h_test = (f_inv_mod_q * cand_g) % q
print("h matches?", h_test == h)

# 3) 用找到的 f,g 解密 m
a = (cand_f * e) % q
# 计算 f 的逆模 g，然后 m = a * f^{-1} mod g
f_inv_mod_g = pow(cand_f, -1, cand_g)
m = (a * f_inv_mod_g) % cand_g

print("Recovered m (bitlen):", m.bit_length())
print("Flag bytes:", long_to_bytes(m))
