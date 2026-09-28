
from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms


# ============================================================
# PATHS
# ============================================================

TRAIN_DIR = Path("data/processed/train")
VAL_DIR = Path("data/processed/val")
MODEL_DIR = Path("models")

MODEL_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# TRAINING SETTINGS
# ============================================================

BATCH_SIZE = 8
NUM_EPOCHS = 1
IMAGE_SIZE = 224
NUM_WORKERS = 0

device = torch.device("cpu")

print(f"Using device: {device}")


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

train_transforms = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

val_transforms = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])


# ============================================================
# LOAD DATASETS
# ============================================================

train_dataset = datasets.ImageFolder(
    TRAIN_DIR,
    transform=train_transforms
)

val_dataset = datasets.ImageFolder(
    VAL_DIR,
    transform=val_transforms
)


train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=NUM_WORKERS
)


num_classes = len(train_dataset.classes)
class_names = train_dataset.classes

print(f"Classes: {num_classes}")
print(f"Training images: {len(train_dataset)}")
print(f"Validation images: {len(val_dataset)}")


# ============================================================
# CREATE MODEL
# ============================================================

model = models.efficientnet_b0(weights=None)

input_features = model.classifier[1].in_features

model.classifier[1] = nn.Linear(
    input_features,
    num_classes
)

model = model.to(device)


# ============================================================
# LOSS FUNCTION AND OPTIMIZER
# ============================================================

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# ============================================================
# TRAINING
# ============================================================

for epoch in range(NUM_EPOCHS):

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    print(f"\nStarting epoch {epoch + 1}/{NUM_EPOCHS}")

    for batch_index, (images, labels) in enumerate(train_loader):

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        predictions = outputs.argmax(dim=1)

        total += labels.size(0)

        correct += (
            predictions == labels
        ).sum().item()


        # Print progress every 100 batches

        if (batch_index + 1) % 100 == 0:

            print(
                f"Batch {batch_index + 1}: "
                f"loss={loss.item():.4f}"
            )


        # ====================================================
        # SAVE CHECKPOINT EVERY 500 BATCHES
        # ====================================================

        if (batch_index + 1) % 500 == 0:

            checkpoint_path = (
                MODEL_DIR
                / f"checkpoint_batch_{batch_index + 1}.pth"
            )

            torch.save({

                "model_state_dict": model.state_dict(),

                "optimizer_state_dict": optimizer.state_dict(),

                "epoch": epoch,

                "batch": batch_index + 1,

                "classes": class_names,

                "num_classes": num_classes,

            }, checkpoint_path)

            print(
                f"Checkpoint saved to: "
                f"{checkpoint_path}"
            )


    # ========================================================
    # EPOCH SUMMARY
    # ========================================================

    accuracy = 100 * correct / total

    average_loss = (
        running_loss / len(train_loader)
    )

    print(
        f"\nEpoch {epoch + 1}/{NUM_EPOCHS} completed"
    )

    print(
        f"Average Loss: {average_loss:.4f}"
    )

    print(
        f"Training Accuracy: {accuracy:.2f}%"
    )


# ============================================================
# SAVE FINAL MODEL
# ============================================================

model_path = MODEL_DIR / "efficientnet_b0_test.pth"

torch.save({

    "model_state_dict": model.state_dict(),

    "classes": class_names,

    "num_classes": num_classes,

}, model_path)


print("\nTraining completed successfully!")

print(
    f"Model saved to: {model_path}"
)