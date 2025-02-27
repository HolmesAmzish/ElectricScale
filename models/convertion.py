import torch.onnx
import torch
import torchvision.models as models

"""
File: models/convertion.py
Date: 2025-02-24
Author: SHENG
"""

# Load model
model = torch.load("model.pth", weights_only=False)
model.eval()
print(model)

# Prepare an example tensor
batch_size = 1
channels = 3
height = 128
width = 128

example_input = torch.rand(batch_size, channels, height, width)

# Save model as Onnx model
onnx_model_path = "./vegetable_classification_model.onnx"
torch.onnx.export(
    model,
    example_input,
    onnx_model_path,
    export_params=True,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
)

print(f"Model has been converted to ONNX format and saved as {onnx_model_path}")
