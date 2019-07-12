import numpy as np

# %%
arr = np.empty((10, 10))
for i in range(10):
    arr[i] = i

arr_unique = np.unique(arr)  # distinct操作
arr_in1d = np.in1d([10, 1, 11, 2], arr)  # 判断前者元素是否是后者的成员
arr_intersect1d = np.intersect1d([10, 1, 11, 2], arr)  # 求交集
arr_union1d = np.union1d([10, 1, 11, 2], arr)  # 求并集
arr_diff = np.setdiff1d([10, 1, 11, 2], arr)  # 求差集
arr_diff_cross = np.setxor1d([10, 1, 11, 2], arr)  # 求对称差
