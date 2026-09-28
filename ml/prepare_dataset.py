from pathlib import Path
import random
import shutil

SOURCE = Path("data/PlantVillage/raw/color")
OUTPUT = Path("data/processed")

TRAIN_RATIO = 0.8
SEED = 42

random.seed(SEED)

if not SOURCE.exists():
    raise FileNotFoundError(f"Dataset folder not found: {SOURCE}")

categories = sorted(
    folder for folder in SOURCE.iterdir()
    if folder.is_dir()
)

print(f"Found {len(categories)} categories")

total_train = 0
total_val = 0

for category in categories:
    images = [
        file for file in category.rglob("*")
        if file.is_file()
        and file.suffix.lower() in {".jpg", ".jpeg", ".png"}
    ]

    random.shuffle(images)

    split_index = int(len(images) * TRAIN_RATIO)

    train_images = images[:split_index]
    val_images = images[split_index:]

    train_dir = OUTPUT / "train" / category.name
    val_dir = OUTPUT / "val" / category.name

    train_dir.mkdir(parents=True, exist_ok=True)
    val_dir.mkdir(parents=True, exist_ok=True)

    for image in train_images:
        shutil.copy2(image, train_dir / image.name)

    for image in val_images:
        shutil.copy2(image, val_dir / image.name)

    total_train += len(train_images)
    total_val += len(val_images)

    print(
        f"{category.name}: "
        f"{len(train_images)} train, "
        f"{len(val_images)} validation"
    )

print("\nDataset preparation completed!")
print(f"Training images: {total_train}")
print(f"Validation images: {total_val}")
