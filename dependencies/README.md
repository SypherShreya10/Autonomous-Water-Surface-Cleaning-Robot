# Dependencies

This folder contains the external dependencies that were used while deploying the trained YOLOv5 TensorFlow Lite model on a Raspberry Pi 3 Model B.

These files are included because finding compatible TensorFlow Lite runtime packages for Raspberry Pi 3 can be challenging. During the development of this project, installing TensorFlow Lite using `pip` frequently resulted in compatibility issues due to Python version mismatches and unavailable ARM wheels.

To simplify the setup process and make this repository fully reproducible, the working wheel files used during development are provided here.

If newer official versions are available, they may be used instead.

---

## Folder Contents

| File | Description |
|------|-------------|
| `tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl` | TensorFlow Lite Runtime for Python 3.7 on Raspberry Pi (32-bit ARMv7) |
| `tflite_runtime-2.5.0.post1-cp39-cp39-linux_armv7l.whl` | TensorFlow Lite Runtime for Python 3.9 on Raspberry Pi (32-bit ARMv7) |

---

## Why TensorFlow Lite?

Running the complete TensorFlow framework on a Raspberry Pi 3 is not recommended because:

- TensorFlow consumes significant RAM.
- Installation is time-consuming.
- Performance is considerably slower.
- Raspberry Pi 3 has limited computational resources.

TensorFlow Lite provides:

- Faster inference
- Lower memory consumption
- Smaller deployment size
- Better compatibility with embedded systems

For these reasons, the trained YOLOv5 model was converted into a TensorFlow Lite (`.tflite`) model before deployment.

---

## Choosing the Correct Wheel File

The correct wheel depends on the Python version installed on your Raspberry Pi.

| Python Version | Wheel File |
|---------------|------------|
| Python 3.7 | `tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl` |
| Python 3.9 | `tflite_runtime-2.5.0.post1-cp39-cp39-linux_armv7l.whl` |

To check your Python version, run:

```bash
python3 --version
```

---

## Installation

Navigate to this folder and install the appropriate wheel.

### Python 3.7

```bash
pip3 install tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
```

### Python 3.9

```bash
pip3 install tflite_runtime-2.5.0.post1-cp39-cp39-linux_armv7l.whl
```

---

## Verify Installation

Run:

```bash
python3
```

Then:

```python
import tflite_runtime.interpreter as tflite
print("TensorFlow Lite installed successfully!")
```

If no errors appear, the installation was successful.

---

# Common Errors

## ERROR:

```
is not a supported wheel on this platform
```

### Cause

The wheel file does not match your installed Python version or system architecture.

### Solution

First check your Python version:

```bash
python3 --version
```

Then install the matching wheel.

---

## ERROR

```
ModuleNotFoundError:
No module named 'tflite_runtime'
```

### Solution

Install the appropriate wheel again using:

```bash
pip3 install <wheel_file_name>
```

---

## ERROR

```
Illegal instruction
```

### Cause

An incompatible wheel was installed.

### Solution

Ensure you are using:

- Raspberry Pi 3
- Raspberry Pi OS (32-bit)
- ARMv7 wheel

---

## Important Notes

These wheel files were tested during the development of this project on:

- Raspberry Pi 3 Model B
- Raspberry Pi OS (32-bit Legacy)
- ARMv7 architecture

Compatibility with newer Raspberry Pi models or 64-bit operating systems is not guaranteed.

---

## Why are these files included?

Normally, third-party dependencies are not stored inside a GitHub repository.

However, Raspberry Pi users frequently encounter issues locating compatible TensorFlow Lite Runtime wheels, especially for older hardware such as the Raspberry Pi 3.

These files are included solely to simplify the reproduction of this project and to save future users from the installation issues encountered during development.

---

## Next Step

After successfully installing TensorFlow Lite Runtime, proceed to the [`raspberry_pi`](../raspberry_pi) folder to set up the Raspberry Pi deployment environment and run real-time waste detection.