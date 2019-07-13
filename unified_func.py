import numpy as np

# %%
# 元素级数组函数，即对数组中每个元素其作用的函数，可以看做简单函数的矢量化包装器
# 又根据函数参数的个数分为一元和二元函数
arr = np.arange(10)
arr_sqrt = np.sqrt(arr)  # 对矩阵中的每个元素求平方根
arr_exp = np.exp(arr)  # 对矩阵中的每个元素求自然底数e的x次方

x = np.random.randn(4, 4)
arr_mod, arr_div = np.modf(x)  # 返回小数位与整数两个矩阵

arr_abs = np.abs(x)  # 求绝对值，対复数起效
arr_fabs = np.fabs(x)  # 求绝对值，对非复数起效，速度更快

arr_sign = np.sign(x)  # 获得正负号

arr_ceil = np.ceil(x)  # 向上取整
arr_floor = np.floor(x)  # 向下取整
arr_rint = np.rint(x)  # 四舍五入

arr_isnull = np.isnan(x)  # 返回是否为空值的bool型数组
# 其他还有 isinf(判断是否无穷)，log,log10,cos,sin，arccos等函数，此处仅列举常见的函数

# %%
x = np.random.randn(8)
y = np.random.randn(8)
z = np.maximum(x, y)  # 二元函数，求两个相同shape的矩阵中对应元素的最大值并返回矩阵
x[0] = np.nan
arr_fmax = np.fmax(x, y)  # 忽略nan值的max函数,对于空值不进行比较，返回另外一个值
arr_min = np.minimum(x, y)  # 会返回空值
arr_fmin = np.fmin(x, y)

arr_add = np.add(x, y)  # 等价于使用加号
arr_multiply = np.multiply(x, y)  # 等价于使用乘号
arr_div = np.divide(x, y)  # 等价于使用除号
arr_power = np.power(x, y)  # 对于x的元素求y次方
arr_copysign = np.copysign(x, y)  # 将第二个数组中的符号复制给第一个数组
