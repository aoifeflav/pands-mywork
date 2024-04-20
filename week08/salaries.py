#salaries.py
#Author: Aoife Flavin

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
no_of_entries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, no_of_entries)

salaries_plus = salaries + 5000

salaries_mult = salaries * 1.05

new_salaries = salaries_mult.astype(int)
#print(new_salaries)

plt.hist(salaries)
plt.show()

