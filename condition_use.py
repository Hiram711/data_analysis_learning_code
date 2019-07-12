# /usr/bin/env/python3
# -*-coding:utf-8-*-
# %%
import numpy as np

xarr = np.arange(1.1, 1.6, 0.1)
yarr = np.arange(2.1, 2.6, 0.1)
cond = np.array([True, False, True, True, False])

# %%
# 当cond为真时从x取值，否则从y取值
result1 = [x if c else y for x, y, c in zip(xarr, yarr, cond)]  # 传统做法,纯python实现速度慢，不支持多维数组
result2 = np.where(cond, xarr, yarr)  # 利用where函数实现

# %%
# where第二第三个参数还可以是标量值
arr = np.random.randn(4, 4)
arr2 = np.where(arr > 0, 2, -2)  # 将正值设为2，负值设为-2
arr3 = np.where(arr > 0, 2, arr)  # 只将正值设为2

# where可以嵌套使用
