from .train_generator import Generator, nz
import torch
import matplotlib.pyplot as plt
import torchvision.utils as vutils
import numpy as np


ngpu = 0
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")

# Create the generator
netG = Generator(ngpu).to(device)

# Handle multi-GPU if desired
if (device.type == 'cuda') and (ngpu > 1):
    netG = torch.nn.DataParallel(netG, list(range(ngpu)))

netG.load_state_dict(torch.load("result/gan_weights", map_location=torch.device(device) ))
netG.eval()



fixed_noise = torch.randn(64, nz, 1, 1, device=device)
with torch.no_grad():
    fake = netG(fixed_noise).detach().cpu()
grid = vutils.make_grid(fake, padding=2, normalize=True)

plt.imshow(np.transpose(grid, (1,2,0)))
plt.show()
