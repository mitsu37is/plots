import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn

fig = plt.figure()

ims = []

for i in range(10):
    omega = np.sqrt(3)
    t = np.arange(0, 100, 0.1)  # 100個の乱数を生成
    im = seaborn.scatterplot(np.sin(omega * t), np.sin(t))             # 乱数をグラフにする
    ims.append(im)                  # グラフを配列 ims に追加

# 10枚のプロットを 100ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=100)
plt.show()