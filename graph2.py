import numpy as np
import matplotlib.pyplot as plt

fst_logp = np.array([0.21, 0.30, 0.35, 0.41, 0.45, 0.50,
                0.63, 0.71, 0.81, 1.01, 1.11, 1.22,
                1.42, 1.52, 1.60, 1.63])
fst_m = np.array([16.8, 16.7, 16.3, 16.0, 16.1, 16.0,
                  15.6, 15.6, 15.2, 14.3, 14.7, 13.8,
                  13.8, 13.4, 13.6, 13.1])
trd_logp = np.array([0.29, 0.49, 0.69, 0.73, 0.74, 0.83,
                     0.90, 0.99, 1.04, 1.13, 1.62])
trd_m = np.array([-2.54, -2.62, -3.08, -3.54, -3.91, -3.93,
                  -3.84, -4.03, -4.34, -4.71, -5.95])
plt.xlabel("logP")
plt.ylabel("-m(M)")
plt.plot(fst_logp, fst_m, ".", label="SMC", color="orange")
plt.plot(trd_logp, trd_m, ".", label="standard", color="blue")
plt.ylim(20, -10)
plt.legend()
plt.show()

plt.plot(fst_logp, fst_m, ".", label="SMC", color="orange")
plt.ylim(17, 12.5)
plt.legend()
plt.show()

plt.plot(trd_logp, trd_m, ".", label="standard", color="blue")
plt.ylim(-2, -6.5)
plt.legend()

fit = np.polyfit(trd_logp, trd_m, 1)
x = np.arange(0.2, 1.7, 0.1)
y = fit[0] * x + fit[1]
plt.plot(x, y)
plt.scatter(1.3, fit[0] * 1.3 + fit[1], color="red")
plt.show()