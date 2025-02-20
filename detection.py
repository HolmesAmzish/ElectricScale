import cv2
import numpy as np
import torch
from torch import nn
from torchvision import transforms, models
from PIL import Image


model = torch.load("models/model.pth", weights_only=False)
model.eval()
# print(model)

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(0, 1)
])


def classify_by_image(frame_rgb):
    """
    :param frame_rgb:
    :return: class_idx: classification index result of input image
    """
    frame_rgb = Image.fromarray(frame_rgb)
    frame_tensor = transform(frame_rgb).unsqueeze(0)

    with torch.no_grad():
        output = model(frame_tensor)
        _, predicted = torch.max(output, 1)

    class_idx = predicted.item()
    return class_idx
