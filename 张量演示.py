import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 生成数据
tensor_0d = np.array(5)  
tensor_1d = np.array([1, 2, 3])  
tensor_2d = np.array([[1, 2, 3], [4, 5, 6]])  
tensor_3d = np.stack([tensor_2d, tensor_2d])  # 增加一个维度，得到 3D

# 定义要展示的张量
tensors = [tensor_0d, tensor_1d, tensor_2d, tensor_3d]
titles = ["0D (标量)", "1D (向量)", "2D (矩阵)", "3D (立方体)"]

# 创建画布
fig, ax = plt.subplots()

def update(i):
    ax.clear()
    tensor = tensors[i]
    title = titles[i]

    # 0D（标量）
    if tensor.ndim == 0:
        ax.text(0.5, 0.5, str(tensor), fontsize=30, ha='center', va='center')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    # 1D（向量）
    elif tensor.ndim == 1:
        ax.plot(tensor, 'ro-', markersize=10)
        ax.set_xticks(range(len(tensor)))
        ax.set_yticks([])

    # 2D（矩阵）
    elif tensor.ndim == 2:
        ax.matshow(tensor, cmap="Blues")
        for (i, j), val in np.ndenumerate(tensor):
            ax.text(j, i, f"{val}", ha='center', va='center', fontsize=20)

    # 3D（立方体）
    elif tensor.ndim == 3:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.text(0.5, 0.5, "3D 数据\n多个矩阵堆叠", fontsize=20, ha='center', va='center')

    ax.set_title(title, fontsize=15)

ani = animation.FuncAnimation(fig, update, frames=len(tensors), interval=1500)
plt.show()
