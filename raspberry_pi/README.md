# Raspberry Pi Deployment

This folder contains the Python scripts used to deploy the trained YOLOv5 TensorFlow Lite model on a Raspberry Pi 3 Model B.

The deployment workflow consists of three stages:

1. Testing the model on a single image.
2. Running real-time object detection using a USB webcam.
3. Streaming the live detection feed through a Flask web application.

The scripts provided here are the exact scripts used during the development of this project.

---

# Folder Contents

| File | Description |
|------|-------------|
| `testimg.py` | Tests the TensorFlow Lite model on a single image. Useful for verifying that the model is working correctly before testing with a webcam. |
| `testrun.py` | Performs real-time object detection using a USB webcam connected to the Raspberry Pi. |
| `telecast.py` | Starts a Flask server that streams the webcam feed with real-time detections, allowing the output to be viewed from another device on the same network. |

---

# Hardware Used

- Raspberry Pi 3 Model B
- Raspberry Pi OS (32-bit Legacy)
- USB Webcam
- MicroSD Card (16 GB or higher recommended)
- Stable 5V 2.5A Power Supply

---

# Software Requirements

- Python 3.9
- OpenCV
- NumPy
- Flask
- TensorFlow Lite Runtime

The required TensorFlow Lite Runtime wheel files are available in the `dependencies` folder.

---

# Raspberry Pi Folder Structure

During development, the following directory structure was used on the Raspberry Pi.

```
/home/pi/yolo_stream/

│── telecast.py
│── testrun.py
│── testimg.py
│── yolo_model.tflite
│── labelmap.txt
```

The scripts currently reference this directory.

If you decide to store the files in a different location on your Raspberry Pi, update the file paths inside the scripts accordingly.

---

# Deployment Workflow

```
Train YOLOv5 Model
        │
        ▼
Convert Model to TensorFlow Lite
        │
        ▼
Copy Model to Raspberry Pi
        │
        ▼
Install TensorFlow Lite Runtime
        │
        ▼
Test on Image
        │
        ▼
Test on Webcam
        │
        ▼
Run Flask Stream
```

---

# Step 1 – Install the Dependencies

Install the required Python packages.

```bash
pip3 install numpy
pip3 install opencv-python
pip3 install flask
```

Install TensorFlow Lite Runtime using the appropriate wheel from the `dependencies` folder.

Refer to:

```
dependencies/README.md
```

for detailed installation instructions.

---

# Step 2 – Copy the Required Files

Copy the following files to your Raspberry Pi.

```
telecast.py
testrun.py
testimg.py
yolo_model.tflite
labelmap.txt
```

Place them inside:

```
/home/pi/yolo_stream/
```

or modify the paths in the scripts if you choose a different directory.

---

# Step 3 – Test the Model on an Image

Before testing the webcam, verify that the model loads correctly.

Place a test image inside the same folder.

For this project:

```
plastic_bottle1.jpeg
```

Run:

```bash
python3 testimg.py
```

If the setup is correct, the script will:

- Load the TensorFlow Lite model
- Detect floating waste in the image
- Display the detection result with bounding boxes

---

# Step 4 – Test Live Webcam Detection

Connect a USB webcam to the Raspberry Pi.

Run:

```bash
python3 testrun.py
```

The script will:

- Capture frames from the webcam
- Run YOLOv5 inference
- Display detections in real time
- Draw bounding boxes with confidence scores

Press **Q** to exit.

---

# Step 5 – Stream the Detection Feed

To view the detection output remotely, run:

```bash
python3 telecast.py
```

The Flask server will start on port **5000**.

Find the Raspberry Pi's IP address:

```bash
hostname -I
```

Open a browser on another device connected to the same Wi-Fi network and visit:

```
http://<raspberry_pi_ip>:5000
```

The live detection stream should now be visible.

---

# Auto-Start on Boot (Optional)

This project also supports automatically starting the Flask application whenever the Raspberry Pi boots.

The required `systemd` service configuration and setup commands are provided in:

```
setup_autostart.txt
```

Rename the service file if required and follow the commands provided to:

- Reload systemd
- Enable the service
- Start the service automatically during boot

This allows the robot to begin streaming immediately after powering on, without manually running the Python script.

---

# Common Issues

## TensorFlow Lite Runtime Installation Error

Example:

```
is not a supported wheel on this platform
```

### Cause

The installed wheel does not match the Python version on the Raspberry Pi.

### Solution

Check your Python version:

```bash
python3 --version
```

Then install the corresponding wheel from the `dependencies` folder.

---

## Webcam Not Detected

Check whether the webcam is detected.

```bash
ls /dev/video*
```

If no device appears:

- reconnect the webcam
- try another USB port
- verify the webcam works using another application

---

## ModuleNotFoundError

Example:

```
No module named 'tflite_runtime'
```

Install the correct TensorFlow Lite Runtime wheel from the `dependencies` folder.

---

## Model File Not Found

If you see:

```
FileNotFoundError
```

verify that:

- `yolo_model.tflite`
- `labelmap.txt`

exist in the expected directory.

---

## Flask Page Does Not Open

Verify that:

- Raspberry Pi and client device are connected to the same network.
- Port **5000** is not blocked.
- The correct Raspberry Pi IP address is being used.

---

# Performance Notes

This project was deployed on a Raspberry Pi 3 Model B.

For optimal performance:

- Use Raspberry Pi OS (32-bit Legacy).
- Close unnecessary background applications.
- Ensure adequate power supply.
- Use the TensorFlow Lite model included in this repository.

---

# Related Folders

| Folder | Purpose |
|---------|---------|
| `training/` | YOLOv5 training notebook used to train the model. |
| `model/` | Trained models in PyTorch, ONNX, and TensorFlow Lite formats. |
| `dependencies/` | TensorFlow Lite Runtime wheels required for Raspberry Pi deployment. |

---

# Research Paper

A detailed explanation of the complete system architecture, methodology, and experimental results is available in the published research paper.

The paper can be accessed from the main project `README.md`.

---

# Next Step

After successfully deploying the model on the Raspberry Pi, proceed to the main project README to understand the complete robot architecture, hardware integration, Arduino communication, and autonomous waste collection workflow.