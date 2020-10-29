# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10.0, 10.0, 0.01)
y = np.exp(x)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(x, y)
plt.show()