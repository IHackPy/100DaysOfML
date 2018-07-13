import torch

# set requires_grad=True

x = torch.ones(2,2, requires_grad=True)

print(x)

# operations 

y = x+2

print("Value of Y = ")
print(y)

# Y was created because of operations on X

print(y.grad_fn)

# More operations on Y
z = y*y*3
out = z.mean()
print(z)
print(out)
print(z.grad_fn)
