from __future__ import print_function
import torch
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

# use torch.device
if torch.cuda.is_available():
	device = torch.device("cuda")
	y = torch.ones_like(x, device=device)
	x = x.to(device)
	z = x+y
	print(z)
	print(z.to("cpu",torch.double))
