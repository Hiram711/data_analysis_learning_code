import numpy as np

# %%
arr = np.arange(16).reshape(4, 4)

# %%
# 将数据保存为二进制文件
np.save('test_array', arr)

# %%
# 从npy文件中读取数组
del arr
arr = np.load('test_array.npy')

# %%
arr2 = np.arange(16).reshape(2, 8)
np.savez('test_arrays.npz', a=arr, b=arr2)  # 以字典形式保存多个数组
arr_dict = np.load('test_arrays.npz')
print(arr_dict['a'])
np.genfromtxt()

# 同时还有np.loadtxt,np.savetxt等类似操作，还有np.genfromtxt进行定制化的文件读取操作
