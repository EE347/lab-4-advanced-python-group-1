import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(0, 10, 101)
np.save("task_7_sin.npy", np.sin(x))
np.save("task_7_cos.npy", np.cos(x))
print(x)

