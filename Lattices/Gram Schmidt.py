import numpy as np

# 定义向量
v1 = np.array([4, 1, 3, -1], dtype=float)
v2 = np.array([2, 1, -3, 4], dtype=float)
v3 = np.array([1, 0, -2, 7], dtype=float)
v4 = np.array([6, 2, 9, -5], dtype=float)

# Gram-Schmidt 正交化
def gram_schmidt(vectors):
    U = []
    for v in vectors:
        u = v.copy()
        for uj in U:
            mu = np.dot(v, uj) / np.dot(uj, uj)
            u -= mu * uj
        U.append(u)
    return U

# 计算
vectors = [v1, v2, v3, v4]
U = gram_schmidt(vectors)

# 提取 u4 的第二个分量
u4 = U[3]
second_component = u4[1]
second_component_5sf = float(f"{second_component:.5g}")
print(second_component_5sf)
