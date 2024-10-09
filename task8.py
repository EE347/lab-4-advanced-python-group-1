import numpy as np
import matplotlib.pyplot as plt

with open("task_7_cos.npy", "r") as f1:
    data1 = f1.read()
    f1.close()

with open("task_7_sin.npy", "r") as f2:
    data2 = f2.read()
f2.close()

plt.plot(data1)
plt.plot(data2)