import numpy as np

# %%
arr = np.random.randn(10)
print(arr)
arr.sort()  # 直接调用sort会改变数组
print(arr)

# %%
arr1 = np.random.randn(10)
print(np.sort(arr1))  # 此种情况下创建副本，不影响原数组
print(arr1)

# %%
arr2d = np.random.randn(4, 4)
arr2d.sort(0)  # 对0轴上的元素进行paix
print(arr2d)
