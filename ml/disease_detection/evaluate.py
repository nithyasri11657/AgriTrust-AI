
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms


# Paths
VAL_DIR = Path("data/processed/val")
MODEL_PATH = Path("models/efficientnet_b0_test.pth")

# Settings
BATCH_SIZE = 8
IMAGE_SIZE = 224

device = torch.device("cpu")

print(f"Using device: {device}")

# Image preprocessing
val_transforms = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# Load validation dataset
val_dataset = datasets.ImageFolder(
    VAL_DIR,
    transform=val_transforms
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=0
)

# Load saved model
checkpoint = torch.load(
    MODEL_PATH,
    map_location=device,
    weights_only=False
)

class_names = checkpoint["classes"]
num_classes = checkpoint["num_classes"]

model = models.efficientnet_b0(weights=None)

input_features = model.classifier[1].in_features

model.classifier[1] = nn.Linear(
    input_features,
    num_classes
)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model = model.to(device)
model.eval()

# Evaluate
correct = 0
total = 0

print("Starting evaluation...")

with torch.no_grad():

    for images, labels in val_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        predictions = outputs.argmax(dim=1)

        total += labels.size(0)

        correct += (
            predictions == labels
        ).sum().item()

accuracy = 100 * correct / total

print("\nEvaluation completed!")
print(f"Correct predictions: {correct}")
print(f"Total images: {total}")
print(f"Validation Accuracy: {accuracy:.2f}%")