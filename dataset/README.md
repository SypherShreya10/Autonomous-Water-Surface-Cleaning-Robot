# Dataset

This folder contains the dataset configuration used to train the YOLOv5 model for the **Autonomous Water Surface Cleaning Robot (AWSCR)**.

Due to GitHub storage limitations, the complete image dataset is **not included** in this repository. Instead, a download link has been provided so that anyone can reproduce the complete training pipeline.

---

# Folder Contents

| File | Description |
|------|-------------|
| `data.yaml` | Dataset configuration file used during YOLOv5 training. |
| `Dataset_Link.txt` | Contains the Google Drive link for downloading the complete dataset. |

---

# Dataset Overview

The dataset consists of images collected from water bodies containing both floating waste and naturally occurring floating objects.

The primary objective of the dataset is not only to detect floating waste but also to help the robot distinguish waste from environmentally important objects such as aquatic vegetation and other natural floating materials.

Examples of objects represented during dataset preparation include:

- Plastic bottles
- Plastic wrappers
- Paper waste
- Twigs
- Flowers
- Leaves
- Other floating debris commonly found on water surfaces

This distinction enables the robot to make environmentally responsible decisions by targeting waste while avoiding unnecessary interaction with natural aquatic elements whenever possible.

The dataset was prepared specifically for training a lightweight YOLOv5 model that can be deployed on a Raspberry Pi 3 Model B for real-time inference.

---

# Dataset Preparation

The dataset was prepared using **Roboflow**.

The preparation pipeline included:

- Image collection
- Image annotation
- Dataset organization
- Automatic train/validation/test splitting
- YOLOv5-compatible export

The exported dataset was then used directly for training in Google Colab.

---

# Dataset Structure

After downloading the dataset from the link provided in `Dataset_Link.txt`, the folder structure should look similar to:

```
dataset/

│── train/
│── valid/
│── test/
│── data.yaml
```

Each split contains:

- Images
- Corresponding YOLO annotation files

---

# Dataset Configuration

The `data.yaml` file defines:

- Training image directory
- Validation image directory
- Test image directory
- Number of classes
- Class names

This file is used directly by YOLOv5 during training.

If you relocate the dataset, update the paths inside `data.yaml` before starting training.

---

# Downloading the Dataset

Open:

```
Dataset_Link.txt
```

Download the dataset from the provided Google Drive link.

Extract the ZIP file.

Ensure that the extracted folder structure matches the one shown above before running the training notebook.

---

# Using the Dataset

The dataset is used during the model training stage.

After downloading:

1. Extract the dataset.
2. Open the Google Colab notebook in the `training` folder.
3. Update the dataset path if necessary.
4. Start training.

The notebook automatically reads the `data.yaml` configuration.

---

# Notes

- The dataset has been exported in YOLOv5 format.
- All annotations follow the YOLO object detection annotation format.
- If additional images are collected, they should be annotated using the same format before retraining the model.

---

# Research Context

One of the primary objectives of this project is to reduce the environmental impact of automated cleaning systems.

Instead of treating every floating object as waste, the trained YOLOv5 model was developed to identify floating debris while minimizing unnecessary interaction with natural aquatic elements such as leaves, flowers, and other floating vegetation.

This design philosophy improves the ecological safety of the Autonomous Water Surface Cleaning Robot and aligns with the objective of preserving aquatic ecosystems while removing human-generated waste. The methodology and motivation behind this approach are discussed in the accompanying research paper. :contentReference[oaicite:1]{index=1}

---

# Related Folders

| Folder | Purpose |
|---------|---------|
| `training/` | Google Colab notebook used for model training. |
| `model/` | Trained PyTorch, ONNX, and TensorFlow Lite models. |
| `raspberry_pi/` | Raspberry Pi deployment scripts. |

---

# Citation

If you use this dataset for research or academic purposes, please cite the accompanying research paper.

The publication details are available in the main project `README.md`.

---

# Next Step

After downloading the dataset, proceed to the `training` folder and follow the Google Colab notebook to train the YOLOv5 model and reproduce the results.