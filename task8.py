import numpy as np
import matplotlib.pyplot as plt

data1 = np.load("task_7_cos.npy")
data2 = np.load("task_7_sin.npy")

plt.title('Sin vs Cos')
plt.xlabel('x vals')
plt.ylabel('y vals')
plt.plot(data1)
plt.plot(data2)
plt.legend()
plt.show()