import numpy as np
import matplotlib.pyplot as plt

import random
import tf_idf_1
import tf_idf_2
import tf_idf_3
import tf_idf_4

# 基础设置
plt.subplot(1, 1, 1)
plt.figure(figsize=(10, 10))

# 设置标题、横轴、纵轴
plt.title("COVID-19背景下2019.12-2020.6期间网络社会心态阶段性变化", loc="center",
          fontdict={'weight': 'normal', 'size': 20})
plt.xlabel('时间阶段', fontdict={'weight': 'normal', 'size': 13})
plt.ylabel('频率', fontdict={'weight': 'normal', 'size': 13})

# 建立横、纵坐标
x = np.array(["2019.12.08-2020.01.22", "2020.01.23-2020.02.07", "2020.02.10-2020.02.13", "2020.03.10-2020.06"])
y1 = np.array([tf_idf_1.frequencies["高兴"], tf_idf_2.frequencies["高兴"], tf_idf_3.frequencies["高兴"], tf_idf_4.frequencies["高兴"]])
y2 = np.array([tf_idf_1.frequencies["害怕"], tf_idf_2.frequencies["害怕"], tf_idf_3.frequencies["害怕"], tf_idf_4.frequencies["害怕"]])
y3 = np.array([tf_idf_1.frequencies["担心"], tf_idf_2.frequencies["担心"], tf_idf_3.frequencies["担心"], tf_idf_4.frequencies["担心"]])
y4 = np.array([tf_idf_1.frequencies["感激"], tf_idf_2.frequencies["感激"], tf_idf_3.frequencies["感激"], tf_idf_4.frequencies["感激"]])
y5 = np.array([tf_idf_1.frequencies["难过"], tf_idf_2.frequencies["难过"], tf_idf_3.frequencies["难过"], tf_idf_4.frequencies["难过"]])
y6 = np.array([tf_idf_1.frequencies["怀疑"], tf_idf_2.frequencies["怀疑"], tf_idf_3.frequencies["怀疑"], tf_idf_4.frequencies["怀疑"]])
y7 = np.array([tf_idf_1.frequencies["嘲讽"], tf_idf_2.frequencies["嘲讽"], tf_idf_3.frequencies["嘲讽"], tf_idf_4.frequencies["嘲讽"]])
y8 = np.array([tf_idf_1.frequencies["冷漠"], tf_idf_2.frequencies["冷漠"], tf_idf_3.frequencies["冷漠"], tf_idf_4.frequencies["冷漠"]])
y9 = np.array([tf_idf_1.frequencies["祝福"], tf_idf_2.frequencies["祝福"], tf_idf_3.frequencies["祝福"], tf_idf_4.frequencies["祝福"]])
y10 = np.array([tf_idf_1.frequencies["警惕"], tf_idf_2.frequencies["警惕"], tf_idf_3.frequencies["警惕"], tf_idf_4.frequencies["警惕"]])
y11 = np.array([tf_idf_1.frequencies["惊讶"], tf_idf_2.frequencies["惊讶"], tf_idf_3.frequencies["惊讶"], tf_idf_4.frequencies["惊讶"]])
y12 = np.array([tf_idf_1.frequencies["愧疚"], tf_idf_2.frequencies["愧疚"], tf_idf_3.frequencies["愧疚"], tf_idf_4.frequencies["愧疚"]])
y13 = np.array([tf_idf_1.frequencies["心疼"], tf_idf_2.frequencies["心疼"], tf_idf_3.frequencies["心疼"], tf_idf_4.frequencies["心疼"]])
y14 = np.array([tf_idf_1.frequencies["愤怒"], tf_idf_2.frequencies["愤怒"], tf_idf_3.frequencies["愤怒"], tf_idf_4.frequencies["愤怒"]])
y15 = np.array([tf_idf_1.frequencies["着急"], tf_idf_2.frequencies["着急"], tf_idf_3.frequencies["着急"], tf_idf_4.frequencies["着急"]])

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 解决中文乱码问题

# 设置标记点和连线形式
plt.plot(x, y1, color=(1, 0, 0), linestyle="solid",
         linewidth=1, marker="o", markersize=8, label="高兴")
plt.plot(x, y2, color=(0, 0, 0), linestyle="solid",
         linewidth=1, marker="x", markersize=8, label="害怕")
plt.plot(x, y3, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="*", markersize=8, label="担心")
plt.plot(x, y4, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="D", markersize=8, label="感激")
plt.plot(x, y5, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="d", markersize=8, label="难过")
plt.plot(x, y6, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="+", markersize=8, label="怀疑")
plt.plot(x, y7, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker=">", markersize=8, label="嘲讽")
plt.plot(x, y8, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="<", markersize=8, label="冷漠")
plt.plot(x, y9, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="^", markersize=8, label="祝福")
plt.plot(x, y10, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="v", markersize=8, label="警惕")
plt.plot(x, y11, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="o", markersize=8, label="惊讶")
plt.plot(x, y12, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="s", markersize=8, label="愧疚")
plt.plot(x, y13, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="p", markersize=8, label="心疼")
plt.plot(x, y14, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="h", markersize=8, label="愤怒")
plt.plot(x, y15, color=(random.random(), random.random(), random.random()), linestyle="solid",
         linewidth=1, marker="H", markersize=8, label="着急")

# 绘制点
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y4):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y5):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y6):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y7):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y8):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y9):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y10):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y11):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y12):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y13):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y14):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
for a, b in zip(x, y15):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)

# 导出
plt.grid(True)
plt.legend()
plt.savefig(r"D:\desktop\COVID-19背景下2019.12-2020.6期间网络社会心态阶段性变化.jpg")
plt.show()












