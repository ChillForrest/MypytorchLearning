import torch
import numpy as np
import sys

# tensor_1=torch.tensor([1,2,3])
# tensor_2=torch.tensor([[1,2,3],[4,5,6]])
# tensor_3=torch.tensor([[1,2,3,4]])
# print(tensor_1)
# print(tensor_2)
# print(tensor_1.shape)
# print(tensor_2.shape)
# print(tensor_1.dtype)
# print(tensor_2.dtype)
# tensor_4=torch.cat([tensor_2,tensor_2,tensor_2])

# print(tensor_4)
# print(tensor_4.shape)

# 创建张量
# tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32, requires_grad=True)

# # 张量属性
# print("张量:", tensor)
# print("形状:", tensor.shape)  # (2,3)
# print("维度:", tensor.dim())  # 2
# print("数据类型:", tensor.dtype)  # float32
# print("设备:", tensor.device)  # cpu
# print("是否需要梯度:", tensor.requires_grad)  # True
# print("元素总数:", tensor.numel())  # 6

import torch

# 创建两个矩阵
matrix1 = torch.tensor([[1, 2], [3, 4]])
matrix2 = torch.tensor([[5, 6], [7, 8]])

# 矩阵乘法
matrix_product = torch.matmul(matrix1, matrix2)
print("矩阵乘法结果:")
print(matrix_product)
matrix_product = matrix1 @ matrix2
print("矩阵乘法结果:")
print(matrix_product)
