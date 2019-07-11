import numpy as np

# %%
arr = np.arange(15).reshape(3, 5)
arr_t = arr.T
arr_t[0] = 0  # 数组的转置其实是原数组的视图，对其操作会导致原数组发生改变
assert sum(arr[:, 0]) == 0

# %%
h_arr = np.arange(16).reshape(2, 2, 4)
h_arr_t = h_arr.transpose(1, 0, 2)  # 对于高维数组的转置，需要指定交换的维度，其他与二维数组基本相同
h_arr_t1 = h_arr.swapaxes(1, 0)  # 另外一种转置方法
assert np.array_equal(h_arr_t, h_arr_t1)
