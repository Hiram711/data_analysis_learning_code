import numpy as np

# 需要在pycharm的项目设置tools中打开scientific mode,并且将运行设置中的run in console选项打开
# %%
data1 = range(10)
arr1 = np.array(data1)  # 参数必须是一个序列型对象，不指定dtype的情况下会自动推导
assert arr1.dtype == np.int32

data11 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr11 = np.array(data11)  # 根据嵌套的序列型对象生成一个二维数组
assert arr11.ndim == 2

# %%
arr2 = np.array(data1, dtype=float)  # 指定dtype的情况
assert arr2.dtype == np.float64

# %%
arr2d = np.arange(10).reshape((5, 2))  # 定义一个5*2的数组，元素为从0开始的10个数字
assert arr2d.ndim == 2  # 利用ndim来得到数组的维度
assert arr2d.shape == (5, 2)  # 利用shape来得到数组的形状

# %%
arr_zero1 = np.zeros((2, 2))  # 定义一个2*2的数组，元素都为0
assert arr_zero1.shape == (2, 2)
arr_zero2 = np.zeros_like(arr2d)  # 定义一个与arrr2d拥有相同形状的数组，元素都为0
assert arr_zero2.shape == (5, 2)

# %%
# ones,empty方式创建数组，与上文的zero类似的用法
arr_ones1 = np.ones((2, 2))
arr_ones2 = np.ones_like(arr2d)
arr_empty1 = np.empty((2, 2))  # 只分配空间不填任何值，其实是一些无意义的随机值
arr_empty2 = np.empty_like(arr2d)

# 一些常见数组创建函数与注意事项
# %%
# 使用array方式默认copy输入数据
l = [1, 2, 3]
test_copy_arr1 = np.array(l)
test_copy_arr1[0] = 0
assert test_copy_arr1[0] != l[0]

# %%
# 使用asarray方式时，如果输入为ndarray就不copy
l2 = [1, 2, 3]
test_copy_arr2 = np.asarray(test_copy_arr1)
test_copy_arr2[0] = 15
assert test_copy_arr1[0] == 15

# %%
rang_array = np.arange(1, 10, 2)  # 与range函数相似，但返回的是一个一维的ndarray
eye_array1 = np.eye(2)  # 返回单位矩阵
eye_array2 = np.identity(2)

# %%
# ndarray常见数据类型有int(8,,16,32,64),float(16,32,64,128),complex(64,128,256),
# bool,object,string_,unicode_
# 可以通过astype进行数据类型转换
numeric_string = np.array(['1', '2', '3.5'])
assert numeric_string.dtype == np.dtype('<U3')
numeric_string2 = numeric_string.astype(np.float)
assert numeric_string2.dtype == np.float
assert id(numeric_string2) != id(numeric_string)  # 使用astype时进行了copy操作
