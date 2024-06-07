import sys
import torch
import torchvision.transforms as transforms
import torchvision.datasets as dset
import matplotlib.pyplot as plt
import numpy as np

fold = sys.argv[1]
image_size = 64
dataroot = f"data/synthetic/{fold}"
celeba = dset.ImageFolder(root=dataroot,
                           transform=transforms.Compose([
                               transforms.Resize(image_size),
                               transforms.CenterCrop(image_size),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                           ]))

x = celeba[0][0]
plt.imshow(x)
plt.show()

quit()
torch.utils.data.DataLoader(celeba, batch_size=100)



labels = []
with torch.no_grad():
    for i,data in enumerate(trainloader):
        soft = model(data)
        _, yhat = torch.max(soft, 1)
        yhat = cpu().detach().numpy()
