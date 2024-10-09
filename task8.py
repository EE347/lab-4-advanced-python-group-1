import numpy as np
import matplotlib.pyplot as plt

data1 = np.load("task_7_cos.npy")
data2 = np.load("task_7_sin.npy")

plt.plot(data1)
plt.plot(data2)

plt.show()