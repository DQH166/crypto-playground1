import numpy as np

# 定义向量
v = np.array([846835985, 9834798552], dtype=np.int64)
u = np.array([87502093, 123094980], dtype=np.int64)

def gauss_lattice_reduction(v1, v2):
    while True:
        # 步骤 (a): 如果 ||v2|| < ||v1||，交换
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            v1, v2 = v2, v1
        # 步骤 (b): 计算 m
        m = int(round(np.dot(v1, v2) / np.dot(v1, v1)))
        # 步骤 (c): 如果 m == 0，返回
        if m == 0:
            return v1, v2
        # 步骤 (d): 更新 v2
        v2 = v2 - m * v1

# 应用 Gauss 算法
v1_new, v2_new = gauss_lattice_reduction(v, u)

# 计算 flag = 内积
flag = np.dot(v1_new, v2_new)
print(flag)
