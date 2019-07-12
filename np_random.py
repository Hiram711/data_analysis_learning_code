import numpy as np

# %%
np.random.seed()  # 产生随机数种子，若指定种子的值，将会产生相同的随机数
l = [1, 2, 3, 4]
np.random.shuffle(l)  # 对序列进行随机排列
print(l)

# %%
l = [1, 2, 3, 4]
l1 = np.random.permutation(l)  # 对序列进行随机排列后返回一个新的序列，原序列不变
print(l1)

# %%
arr_rand = np.random.rand(10)  # 均匀分布随机值
arr_randint = np.random.randint(1, 20, (4, 4))  # 随机整数
arr_randn = np.random.randn(2, 4)  # 正态分布随机值
arr_bionomial = np.random.binomial(5, 0.1, 1000)  # 二项分布
arr_normal = np.random.normal(0, 0.1, 1000)  # 正态高斯分布

# 还有beta、chisquare、gamma、uniform等方法
