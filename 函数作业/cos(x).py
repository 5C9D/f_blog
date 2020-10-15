# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10.0, 10.0, 0.01)
y = np.cos(x)
plt.plot(x, y)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
