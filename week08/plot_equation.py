#plot_equation.py
#plots the function y = x squared.
#Author: Aoife Flavin

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()