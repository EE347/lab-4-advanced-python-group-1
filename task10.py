import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

data_f = pd.read_csv('task9.csv')

data_f.set_index('Date', inplace=True)

plt.figure(figsize=(12,6))
for company in data_f.columns:
    initial = data_f[company].iloc[0]
    percentage_change = ((data_f[company].iloc[-1] - initial)/initial )* 100
    plt.plot(data_f.index, data_f[company], label = f'{company} ({percentage_change: .2f}%)')

plt.title('Stock price Over Time')
plt.xlabel('Date')
plt.ylabel('Stock price')
plt.legend()
plt.xticks(rotation = 45)
plt.grid()
plt.tight_layout()
plt.show()