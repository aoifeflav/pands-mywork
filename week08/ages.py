#ages.py
#Author: Aoife Flavin

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
no_of_entries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, no_of_entries)
ages = np.random.randint(low = 21, high = 65, size = no_of_entries)

plt.scatter(ages, salaries)

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'r')
plt.title("Random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()
#plt.show()
plt.savefig('prettier_plot.png')