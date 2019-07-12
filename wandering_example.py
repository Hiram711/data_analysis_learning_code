import numpy as np

# %%
# 单人随机漫步
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
walk_min = walk.min()
walk_max = walk.max()
print((np.abs(walk) >= 10).argmax())

# %%
# 多人随机漫步
nsteps = 1000
nwalks = 5000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum(1)
walk_min = walk.min()
walk_max = walk.max()
hit30 = (np.abs(walk) >= 30).any(1)
hit30_counts = np.sum(hit30)

result = (np.abs(walk[hit30]) >= 30).argmax(1)
sr_mean = result.mean()
