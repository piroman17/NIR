import numpy as np
import matplotlib.pyplot as plt

frames = 200
N = int(input("Введите кол-во абонентов\n"))
p = 0.01
T = [0, ]
probability = [0, ]
while p <= 1/N:
    probability.append(p)
    buff = [0]
    # слоты # вероятность успеха # кол-во фреймов
    sum_frames = np.random.binomial(N, p, size=frames)
    for sum_frame in sum_frames:
        res = buff[-1] + sum_frame
        if buff[-1] > 0:
            res -= 1
        buff.append(res)
    T.append(sum(buff)/frames)
    p += 0.01
plt.ylabel('T среднее время')
plt.xlabel('P вероятность')
plt.plot(probability, T)
plt.show()

