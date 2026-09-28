
from pathlib import Path

import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "efficientnet_b0_test.pth"
)

IMAGE_SIZE = 224

device = torch.device("cpu")


# ============================================================
# LOAD MODEL
# ============================================================

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


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

image_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_disease(image_path: str):

    image = Image.open(image_path).convert("RGB")

    image_tensor = image_transform(image)

    image_tensor = image_tensor.unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        confidence, predicted_index = (
            probabilities.max(dim=1)
        )

    predicted_class = class_names[
        predicted_index.item()
    ]

    confidence_value = confidence.item()

    return {
        "disease": predicted_class,
        "confidence": round(
            confidence_value * 100,
            2
        )
    }