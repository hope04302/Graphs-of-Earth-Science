import matplotlib.pyplot as plt
import numpy as np


standard_bv = np.array(list(np.arange(-0.25, 0.10, 0.05)) + list(np.arange(0.10, 1.40, 0.10)))
standard_m = np.array([-2.10, -1.10, -0.30, 0.50, 1.10, 1.50, 1.74, 2.00, 2.45, 2.95, 3.56, 4.23, 4.79,
                       5.38, 5.88, 6.32, 6.78, 7.20, 7.66, 8.11])

pld_bv = np.array([0.085, 0.043, 0.332, 0.118, 0.414, -0.224, -0.297, 0.512, 0.197, -0.225, -0.289, 0.307, 0.067,
                   0.211, 0.487, 0.006, 0.425, 0.369, -0.249, 0.038, -0.215, -0.197, -0.242, 0.526, -0.073, 0.029,
                   0.620, 0.343, 0.527, -0.148, 0.149, 0.339, -0.140, 0.046, -0.133, 0.001, -0.098, -0.031])
pld_m = np.array([8.24, 8.06, 9.6, 8.14, 9.83, 5.44, 3.7, 10.37, 8.56, 5.64, 4.29, 8.97, 8.03,
                  8.58, 10.11, 7.15, 9.7, 9.42, 3.86, 7.85, 5.74, 6.41, 4.17, 10.42, 7.34, 8.09,
                  10.2, 9.27, 10.51, 6.81, 8.37, 9.44, 6.98, 7.64, 7.25, 7.75, 6.8, 6.93])

plt.xlabel("B-V")
plt.ylabel("-m(M)")
plt.title("Homework")
plt.plot(standard_bv, standard_m, ".", label="standard")
plt.plot(pld_bv, pld_m, ".", label="star cluster")
plt.ylim(11, -3)
plt.legend()
plt.show()