import numpy as np

# %%
# 元素级数组函数，即对数组中每个元素其作用的函数，可以看做简单函数的矢量化包装器
# 又根据函数参数的个数分为一元和二元函数
arr = np.arange(10)
arr_sqrt = np.sqrt(arr)  # 对矩阵中的每个元素求平方根
arr_exp = np.exp(arr)  # 对矩阵中的每个元素求自然底数e的x次方

x = np.random.randn(8)
y = np.random.randn(8)
z = np.maximum(x, y)  # 二元函数，求两个相同shape的矩阵中对应元素的最大值并返回矩阵

arr_div, arr_mod = np.modf(x)  # 返回整数与小数位两个矩阵

arr_abs = np.abs(x)  # 求绝对值，対复数起效
arr_fabs = np.fabs(x)  # 求绝对值，对非复数起效，速度更快

arr_sign = np.sign(x)  # 获得正负号

arr_ceil = np.ceil(x)  # 向上取整
arr_floor = np.floor(x)  # 向下取整
arr_rint = np.rint(x)  # 四舍五入
