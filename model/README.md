# Model Files

This folder contains all versions of the trained YOLOv5 model generated during the development and deployment of the **Autonomous Water Surface Cleaning Robot**.

Each model format serves a different purpose in the project, ranging from training to deployment on embedded hardware.

---

# Model Pipeline

```
Dataset
      │
      ▼
YOLOv5 Training
      │
      ▼
best.pt
      │
      ▼
Export to ONNX
      │
      ▼
best.onnx
      │
      ▼
Convert to TensorFlow Lite
      │
      ▼
yolo_model.tflite
      │
      ▼
Deploy on Raspberry Pi 3
```

---

# Folder Contents

| File | Purpose |
|------|---------|
| `best.pt` | Original YOLOv5 model generated after training. Used for retraining, validation, and exporting to other formats. |
| `best.onnx` | ONNX version of the trained model. Useful for interoperability and deployment on platforms supporting the ONNX Runtime. |
| `yolo_model.tflite` | TensorFlow Lite version of the trained model used for deployment on Raspberry Pi 3. |

---

# Model Description

The model was trained to detect floating waste objects on water surfaces using the YOLOv5 object detection framework.

The objective is to enable an autonomous floating robot to identify waste in real time and assist in waste collection while avoiding unnecessary interaction with surrounding aquatic vegetation.

---

# Why Multiple Model Formats?

Different deployment platforms require different model formats.

## 1. best.pt

This is the original PyTorch model produced after YOLOv5 training.

Use this model if you want to:

- Continue training
- Fine-tune the model
- Validate performance
- Export to other formats

---

## 2. best.onnx

The ONNX model provides a framework-independent representation.

It can be used with:

- ONNX Runtime
- NVIDIA TensorRT
- OpenVINO
- Edge devices
- Cross-platform inference

Although it is not directly used in this Raspberry Pi deployment, it has been included for reproducibility and future extensions of the project.

---

## 3. yolo_model.tflite

This is the deployment model used by the Raspberry Pi.

It was selected because TensorFlow Lite offers:

- Lower memory consumption
- Faster inference
- Lightweight runtime
- Better suitability for embedded devices

The Raspberry Pi inference scripts located in the `raspberry_pi` folder use this model.

---

# Training Details

Model Architecture

- YOLOv5

Framework

- PyTorch

Training Environment

- Google Colab

Deployment Platform

- Raspberry Pi 3 Model B

Deployment Framework

- TensorFlow Lite Runtime

---

# Using the Models

## Retraining

Use:

```
best.pt
```

---

## ONNX Deployment

Use:

```
best.onnx
```

---

## Raspberry Pi Deployment

Use:

```
yolo_model.tflite
```

---

# Performance Notes

The TensorFlow Lite model was specifically chosen for Raspberry Pi deployment because running the original PyTorch model directly on a Raspberry Pi 3 results in significantly slower inference and higher memory usage.

Converting the trained model to TensorFlow Lite provides a lightweight deployment suitable for embedded hardware.

---

# Important Notes

- Do **not** edit or rename the model files unless the corresponding inference scripts are updated.
- Ensure that the Raspberry Pi inference scripts reference the correct TensorFlow Lite model path.
# Regenerating the Deployment Model

If you retrain the YOLOv5 model, regenerate the deployment model using the scripts included in this folder.

Conversion pipeline:

best.pt
↓
Export to ONNX
↓
best.onnx
↓
convert_to_tflite.py
↓
TensorFlow SavedModel
↓
savedmodel_to_tflite.py
↓
yolo_model.tflite

---

# Related Files

- Training Notebook: [`training/yolo_clean.ipynb`](../training/yolo_clean.ipynb)
- Raspberry Pi Deployment: [`raspberry_pi`](../raspberry_pi)
- Runtime Dependencies: [`dependencies`](../dependencies)

---

# Citation

If you use these trained models in your research or project, please cite the associated research paper listed in the main project README.