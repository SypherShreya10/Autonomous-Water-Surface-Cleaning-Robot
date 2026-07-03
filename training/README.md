# Model Training

This folder contains the Google Colab notebook used to train the YOLOv5 object detection model for the **Autonomous Water Surface Cleaning Robot**.

The notebook implements the complete training pipeline, starting from dataset preparation and model training to exporting the trained model into multiple deployment formats.

The final output of this training process is a lightweight TensorFlow Lite model that is deployed on a Raspberry Pi 3 Model B for real-time floating waste detection.

---

# Folder Contents

| File | Description |
|------|-------------|
| `yolo_clean.ipynb` | Google Colab notebook containing the complete training and model export pipeline. |

---

# Training Workflow

```
Dataset
      │
      ▼
Google Colab
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
TensorFlow SavedModel
      │
      ▼
TensorFlow Lite
      │
      ▼
Raspberry Pi Deployment
```

---

# Training Environment

The model was trained using the following environment:

- Google Colab
- Python 3
- PyTorch
- YOLOv5
- CUDA-enabled GPU provided by Google Colab
- TensorFlow
- ONNX

---

# Dataset

The model was trained using a custom floating waste detection dataset prepared using **Roboflow**.

The dataset configuration file (`data.yaml`) is available inside the `dataset` folder.

If you wish to train on a different dataset, replace the dataset path inside the notebook and modify the corresponding `data.yaml` configuration.

---

# Training Steps

The notebook performs the following operations.

## Step 1 – Clone YOLOv5

The official YOLOv5 repository is cloned into the Google Colab environment.

---

## Step 2 – Install Dependencies

All required Python packages and YOLOv5 dependencies are installed automatically.

---

## Step 3 – Load the Dataset

The notebook downloads or mounts the dataset and loads the custom `data.yaml` configuration.

---

## Step 4 – Configure Training

The following parameters can be modified before training:

- Model Variant
- Image Size
- Number of Epochs
- Batch Size
- Dataset Path
- Device Configuration

---

## Step 5 – Train the Model

The YOLOv5 model is trained on the custom floating waste dataset.

During training, the notebook generates:

- Training Loss
- Validation Loss
- Precision
- Recall
- mAP Metrics
- Training Curves

---

## Step 6 – Evaluate the Model

After training, the notebook evaluates the model on the validation dataset and saves the best-performing weights.

The primary output is:

```
best.pt
```

---

## Step 7 – Export the Model

The notebook exports the trained model into multiple deployment formats.

Generated files include:

```
best.pt

best.onnx
```

These files are stored inside the `model` folder.

---

## Step 8 – Convert to TensorFlow Lite

The ONNX model is converted into TensorFlow Lite using the conversion scripts available in the `model` folder.

The final deployment model is:

```
yolo_model.tflite
```

This model is used for inference on the Raspberry Pi 3.

---

# Expected Outputs

After completing the notebook successfully, the following files should be generated.

```
best.pt

best.onnx

yolo_model.tflite
```

---

# Training Decisions

This project involved several design choices to balance detection accuracy with the computational limitations of embedded hardware.

### Why YOLOv5?

YOLOv5 provides an excellent balance between detection accuracy and inference speed while offering a mature training pipeline and straightforward export options.

---

### Why YOLOv5 Nano (YOLOv5n)?

The final deployment target for this project is a Raspberry Pi 3 Model B.

Since the Raspberry Pi has limited processing power and memory, the lightweight YOLOv5 Nano model was selected to achieve real-time inference while maintaining acceptable detection accuracy.

---

### Why Google Colab?

Training deep learning models requires GPU acceleration.

Google Colab provides free access to NVIDIA GPUs, significantly reducing training time compared to running the training process on a standard personal computer.

---

### Why TensorFlow Lite?

Although the model is initially trained using PyTorch, deploying the PyTorch model directly on a Raspberry Pi results in higher memory usage and slower inference.

TensorFlow Lite provides:

- Faster inference
- Lower memory consumption
- Smaller model size
- Better compatibility with embedded systems

For these reasons, the trained model is converted into TensorFlow Lite before deployment.

---

### Why ONNX?

The ONNX format acts as an intermediate representation between PyTorch and TensorFlow.

Using ONNX makes it easier to convert the trained model into different deployment formats while maintaining interoperability across multiple frameworks.

---

# Customization

The notebook can easily be adapted for different datasets.

You can modify:

- Dataset
- Number of Classes
- Image Resolution
- Number of Epochs
- Batch Size
- Learning Rate
- YOLOv5 Model Variant

After retraining, regenerate the deployment model by following the conversion process described in the `model` folder.

---

# Notes

This notebook is intended to run on **Google Colab**.

If you wish to execute it locally:

- Install CUDA (if using an NVIDIA GPU).
- Install all required dependencies.
- Update the dataset paths.
- Modify the file paths where necessary.

---

# Related Folders

| Folder | Purpose |
|---------|---------|
| `dataset/` | Dataset configuration used during training. |
| `model/` | Trained models and conversion scripts generated from this notebook. |
| `raspberry_pi/` | Deployment scripts for Raspberry Pi 3. |

---

# Research Paper

The methodology, system architecture, implementation details, and experimental results of this project are discussed in the accompanying research paper.

Links to the published paper are provided in the main project README.

---

# Next Step

Once the model has been trained successfully, proceed to the **model** folder to understand the exported model formats and the conversion pipeline.

Finally, follow the **raspberry_pi** deployment guide to run the TensorFlow Lite model on a Raspberry Pi 3 Model B for real-time floating waste detection.