from __future__ import print_function
import torch
# Create a tensors based on existing tensor.

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5,3, dtype=torch.double)
print(x)

x = torch.randn_like(x, dtype=torch.float)
print(x)

print(x.size())

y = torch.rand(5,3)
print(x+y)
