from math import gcd

# 序列
a = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

# Step 1: 计算所有行列式差值 det = a[i]*a[j+1] - a[i+1]*a[j]
dets = []
n = len(a)
for i in range(n):
    for j in range(i+1, n-1):  # j+1 不要越界
        det = a[i]*a[j+1] - a[i+1]*a[j]
        dets.append(abs(det))

# Step 2: 求所有 det 的最大公约数 (即 p 的候选)
g = 0
for d in dets:
    g = gcd(g, d)

p = g
print("素数 p =", p)

# Step 3: 计算 x
# 利用公式 x ≡ a[i+1] * inv(a[i]) mod p
xs = []
for i in range(n-1):
    ai, aj = a[i], a[i+1]
    if ai % p == 0:
        continue
    inv_ai = pow(ai, -1, p)  # Python 3.8+ 支持 pow(a, -1, mod)
    x = (aj * inv_ai) % p
    xs.append(x)

print("所有计算得到的 x =", xs)
print("最终结果: p =", p, ", x =", xs[0])
