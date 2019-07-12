import numpy as np

# %%
# 矩阵间的运算
arr = np.random.randn(16).reshape(4, 4)

multi1 = arr * arr  # 矩阵点乘，对位相乘
multi2 = arr ** 2  # 从矩阵点乘推演而来，多次对位相乘
multi3 = np.dot(arr, arr)  # 矩阵乘法

# 加减法与矩阵加减法一致，必须形状相同才可以，对位加减即可
diff1 = arr - arr

div1 = arr / arr  # 矩阵点除，必须形状相同才可以，对位相除即可
div2 = np.dot(arr, np.linalg.inv(arr))  # 矩阵除法，仅以二维矩阵为例，可以转化为乘法，即乘以逆矩阵

# %%
# 矩阵与标量间的运算，即广播
scalar_multi = 4 * arr
scalar_div = 4 / arr
scalar_add = 1 + arr  # 全部元素分别加
scalar_diff = 1 - arr

# 线性代数中的运算基本都可以在np.linalg中找到
