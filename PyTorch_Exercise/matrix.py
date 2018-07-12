from __future__ import print_function
import torch

# Construct a  5*3 Matrix , Uninitialized
x = torch.empty(5,3)
print(x)

# Construct a randomely initialized matrix
y = torch.rand(5,3)
print(y)

# Construct a matrix filled with zeros and of d type long
z = torch.zeros(5,3, dtype=torch.long)
print(z)

# Construct a tensor directly from data
z1 = torch.tensor([5.5, 3])
print(z1)
