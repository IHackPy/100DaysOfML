from __future__ import print_function
import torch

a = torch.ones(5)

print(a)

b = a.numpy()
print(b)

# change numpy array in value
a.add_(1)

print(a)
print(b)
