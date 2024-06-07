import pickle
import csv
from torchvision.datasets import VisionDataset


class SyntheticCeleba(VisionDataset):
    def __init__(self, root, target_transform, transform):
        super().__init__(root, transform=transform, target_transform=target_transform)
        self.root = root
        self.attr = self._load_csv(Path(self.t))

    def _load_csv(self, path):
        with open(path) as csv_file:
            data = csv.read(csv_file, delimiter=",")

    def __getitem(self, index):
        with open(Path(self.root, ), 'rb') as f:
            X = pickle.load(f)
        target = self.attr[index]
        if self.target_transform is not None:
                target = self.target_transform(target)


        return X, target

    def __len__(self):
        return len(self.attr)
