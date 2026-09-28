# 🌱 AgriTrust AI

### AI-Powered Smart Agriculture Platform

AgriTrust AI is a smart agriculture platform that combines **Artificial Intelligence, crop disease detection, farm monitoring, and intelligent agricultural insights** to support better crop-health decisions.

The current system allows users to upload a plant leaf image and receive an AI-based disease classification using a trained **EfficientNet-B0** model.

---

## 🎯 Project Objective

Traditional crop disease identification can depend on manual inspection and agricultural expertise.

AgriTrust AI aims to make preliminary crop-health analysis more accessible by combining:

- 🤖 Artificial Intelligence
- 🌱 Plant disease detection
- 📊 Farm condition monitoring
- 📡 Smart agriculture concepts
- 💡 AI-assisted recommendations

The long-term goal is to move from simple disease classification toward **context-aware agricultural decision support**.

---

## ✨ Current Features

### 🔬 AI Plant Disease Detection

Users can upload a JPG or PNG image of a plant leaf.

The trained AI model analyzes the image and returns:

- Predicted plant condition
- AI confidence percentage
- Model information
- Supported disease category

The current model recognizes **38 plant health/disease categories**.

### 📊 Farm Monitoring Dashboard

The dashboard provides a smart-farming interface for displaying farm conditions such as:

- 🌡️ Temperature
- 💧 Humidity
- 🌱 Soil moisture
- 🧪 Soil pH

The current dashboard uses sample sensor values as placeholders for the planned IoT integration.

### ⚡ Fast Local AI Analysis

The trained model runs locally through a FastAPI backend.

The frontend communicates with the backend through an API endpoint for disease prediction.

---

## 🤖 AI Model

AgriTrust AI currently uses:

**EfficientNet-B0**

The model was trained using the PlantVillage dataset's color image subset.

### Model Configuration

| Component | Value |
|---|---|
| Model | EfficientNet-B0 |
| Framework | PyTorch |
| Image Size | 224 × 224 |
| Number of Classes | 38 |
| Training Device | CPU |
| Dataset | PlantVillage |
| Current Evaluated Accuracy | 78.20% |

The reported **78.20% accuracy** is the validation accuracy obtained from the current evaluated model checkpoint on the prepared validation set.

This value should not be interpreted as guaranteed real-world field accuracy.

---

## 📈 Model Evaluation

The current checkpoint was evaluated on:

- **10,876 validation images**
- **8,505 correctly classified images**
- **78.20% validation accuracy**

The model was evaluated on the prepared PlantVillage validation dataset.

Further training and experimentation can be performed to improve the model.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │     User / Farmer    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │   Vite Application   │
                    └──────────┬───────────┘
                               │
                         HTTP API Request
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  EfficientNet-B0 AI  │
                    │   Disease Detection  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prediction +         │
                    │ Confidence Score     │
                    └──────────────────────┘