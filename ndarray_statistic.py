import numpy as np

# %%
arr = np.random.randn(5, 4)
arr_mean = arr.mean()
arr_sum = arr.sum()
arr_std = arr.std()
arr_var = arr.var()
arr_min = arr.min()
arr_max = arr.max()
arr_max_index = arr.argmax()  # 获取最大值的索引，从第一个元素开始数，返回整数
arr_min_index = arr.argmin()  # 获取最小值的索引
arr_cum_sum = arr.cumsum()  # 累计求和
arr_cum_prod = arr.cumprod()  # 累计求乘积

# %%
# 添加axis参数的效果
arr_mean_axis = arr.mean(axis=1)  # 计算在轴1上的平均值
arr_sum_axis = arr.sum(axis=0)  # 计算在轴0上的和
arr_cum_sum_axis = arr.cumsum(0)  # 在轴0上累计求和

# %%
# 对于bool型数组，True为1,False为0
arr1 = np.random.randn(100)
arr_bool = arr1 > 0
arr_bool_sum = arr_bool.sum()  # 数组里有多少个正数
assert arr_bool.any()  # any用于判断bool数组中是否有真值，也可用于非bool数组，非0即为True
assert not arr_bool.all()  # all用于判断bool数组中是否全为真值



