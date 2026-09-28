from datasets import load_dataset

print("Starting PlantVillage dataset download...")

dataset = load_dataset(
    "mohanty/PlantVillage",
    "default",
    download_mode="force_redownload"
)

print("Dataset downloaded successfully!")
print(dataset)

for split in dataset:
    print(split, "images:", len(dataset[split]))
