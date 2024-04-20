#counties.py
# Lists counties, plts on a pie chart
#Author: Aoife Flavin

import numpy as np
import matplotlib.pyplot as plt

potential_counties = ["Cork", "Waterford", "Kerry", "Galway", "Mayo"]

counties = np.random.choice(potential_counties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size = (100))

unique, counts = np. unique(counties, return_counts = True)

#plt.pie(counts, labels = unique)

plt.bar(unique, counts)

plt.show()