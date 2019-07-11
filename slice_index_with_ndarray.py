import numpy as np

# %%
# 对ndarray的普通切片其实是产生了一个视图
l = list(range(10))
arr = np.array(l)
arr1 = arr[0:3]
arr1[:] = 99
assert arr[0] == 99  # 此种切片下，ndarray不产生copy,arr1是arr的一个‘视图’, 对arr1的操作其实是在操作arr
l1 = l[0:3]
l1 = 99, 99, 99
assert l[0] != 99  # 对比python列表，切片会产生copy，操作l1时并不影响l

# %%
# ndarray高维数组的切片
arr2d = np.arange(1, 10).reshape(3, 3)
arr2d1 = arr2d[0]
arr2d2 = arr2d[0:2]
assert arr2d[0, 2] == arr2d[0][2]  # 这两种元素索引方式等价
arr2d3 = arr2d[:2, 1:]  # 利用冒号进行切片，沿着一个方向进行切片用逗号隔开多个方向
assert arr2d3.shape == (2, 2)
arr2d4 = arr2d[1, 1:]  # 整数索引与切片混合使用
assert arr2d4.shape == (2,)

# %%
# bool型索引，要求bool型数组的长度和被索引的轴长度一致
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)  # 随机的7行4列数据，7行对应上面的7个名字
filter_array = names == 'Bob'  # 筛选对用Bob的数据行，产生一个bool型数组
result_array = data[filter_array]  # 将bool型数组作为索引输入要筛选的数据,通过此种方式筛选出的数据将产生copy
result_array[:] = 0
assert data[filter_array][0, 0] != 0  # 因为result_array是产生的copy，所以广播操作并未影响到原来的data数组

filter_array1 = (names == 'Bob') | (names == 'Joe')  # 布尔条件可以通过|，!，&符号使用
result_array1 = data[filter_array1]
assert result_array1.shape == (5, 4)

data[filter_array1] = 0  # 通过bool型索引对数据进行广播
assert data[0, 0] == 0

# %%
# 花式索引，利用整数数组进行索引
fancy_array = np.empty((8, 4))
for i in range(8):
    fancy_array[i] = i

even_array = fancy_array[[0, 2, 4, 6]]  # 通过传入一个整数列表在第一个轴上取偶数列

error_array = fancy_array[[0, 2], [1, 2]]  # 传入多个索引数组，从字面意思来看应当取0,2行1,2列，但是并不是
right_array1 = fancy_array[[0, 2]][:, [1, 2]]  # 这样才能取得预想结果
right_array2 = fancy_array[np.ix_([0, 2], [1, 2])]  # 利用np.ix_也可以

even_array[:] = 99
assert fancy_array[[0, 2, 4, 6]][0, 0] != 99  # 花式索引切片产生了copy，对于copy的广播不会影响原数组
