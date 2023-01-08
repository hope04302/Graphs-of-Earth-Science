import numpy as np
import matplotlib.pyplot as plt

PI = 3.141592
per150 = 140
c = 3 * 10 ** 5

v = np.array([1032.6, 14631.4, 22922.7, 43423.4, 61395.6])

dis_long = np.array([145, 45, 20, 11, 7])
dis_short = np.array([110, 35, 20, 11, 7])
dis = (dis_long + dis_short) / 2
print(f"각지름(mm): {dis}")

dis_degree = dis / per150 * 150
print(f"각지름(도): {dis_degree}")
dis_rad = dis_degree / 3600 * (PI / 180)
print(f"각지름(rad): {dis_rad}")
dis_Mpc = 0.03 / dis_rad
print(f"거리(Mpc): {dis_Mpc}")

plt.title("Hubble")
plt.xlabel("Distance(Mpc)")
plt.ylabel("Velocity(km/s)")
plt.scatter(dis_Mpc, v)

fit = np.polyfit(dis_Mpc, v, 1)
print(f"허블 상수: {fit[0]}")
x = np.arange(0, 850)
y = fit[0] * x + fit[1]
print(f"팽창하는 우주의 크기: {c / fit[0]}")
print(f"팽창하는 우주의 나이: {1 / fit[0] * 3.086e+19 / (86400 * 365)}")

plt.plot(x, y, color="blue")
plt.plot()
plt.show()
