import numpy as np
import matplotlib.pyplot as plt

frames = 5000
N = int(input("Введите кол-во абонентов\n"))
p = 0.01
T = []
probability = []
while p <= (1/N):
    probability.append(p)
    loss = 0
    sum_frames = np.random.binomial(N, p, size=frames)
    for sum_frame in sum_frames:
        if sum_frame > 1:
            # потеряно из-за коллизии
            loss += sum_frame
    T.append(loss/sum(sum_frames))
    p += 0.005
plt.ylabel('p потери пакета')
plt.xlabel('P вероятность')
plt.plot(probability, T)
plt.show()
