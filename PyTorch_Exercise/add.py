from __future__ import  print_function
import torch

x = torch.rand(5,3)
print("Value of X : ")
print(x)

print("Valuee of Y : ")
y = torch.rand(5,3)
print(y)

print("Addition of X and Y : ")

# type 1 Result

print(torch.add(x,y))

print("Secont type of result ")
# type 2 result
result = torch.empty(5,3)
torch.add(x,y, out=result)
print(result)

