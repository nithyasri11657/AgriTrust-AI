
from pathlib import Path

import torch
from torch import nn
from torchvision import models


# Paths
CHECKPOINT_PATH = Path("models/checkpoint_batch_4000.pth")
FINAL_MODEL_PATH = Path("models/efficientnet_b0_test.pth")

# Device
device = torch.device("cpu")

print("Loading checkpoint...")

# Load checkpoint
checkpoint = torch.load(
    CHECKPOINT_PATH,
    map_location=device,
    weights_only=False
)

# Read class information
class_names = checkpoint["classes"]
num_classes = checkpoint["num_classes"]

print(f"Classes: {num_classes}")

# Recreate the same model architecture
model = models.efficientnet_b0(weights=None)

input_features = model.classifier[1].in_features

model.classifier[1] = nn.Linear(
    input_features,
    num_classes
)

# Load trained weights
model.load_state_dict(
    checkpoint["model_state_dict"]
)

model = model.to(device)
model.eval()

# Save final model
torch.save({
    "model_state_dict": model.state_dict(),
    "classes": class_names,
    "num_classes": num_classes,
}, FINAL_MODEL_PATH)

print("Checkpoint loaded successfully!")
print(f"Final model saved to: {FINAL_MODEL_PATH}")
print("Model is ready for evaluation.")