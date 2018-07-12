from __future__ import print_function
import torch

print("x = ")
x = torch.rand(5,3)
print(x)

print("y = ")
y = torch.rand(5,3)
print(y)
y.add(x)

print(y)

# NumPy like indexing 

print(x[:, 1])
