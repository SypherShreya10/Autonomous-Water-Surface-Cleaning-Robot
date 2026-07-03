import cv2
import numpy as np
from tflite_runtime.interpreter import Interpreter

# Load the labels
with open("labelmap.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Load the TFLite YOLO model
interpreter = Interpreter(model_path="yolo_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get input size expected by the model
input_shape = input_details[0]['shape']
input_height, input_width = input_shape[1], input_shape[2]

# Load the test image
image = cv2.imread("plastic_bottle1.jpeg")  # <- change name if needed
if image is None:
    print("❌ Image not found. Make sure 'test.jpg' exists.")
    exit()

# Prepare image
original_height, original_width = image.shape[:2]
resized_image = cv2.resize(image, (input_width, input_height))
input_data = np.expand_dims(resized_image, axis=0).astype(np.uint8)

# Run inference
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Get output
output_data = interpreter.get_tensor(output_details[0]['index'])[0]

for det in output_data:
    if len(det) < 6:
        continue  # Skip malformed data

    x, y, w, h, conf, cls = det[:6]

    if conf < 0.5:
        continue

    # Convert normalized coordinates to pixel values on the original image
    x = x * original_width
    y = y * original_height
    w = w * original_width
    h = h * original_height

    x1 = int(x - w / 2)
    y1 = int(y - h / 2)
    x2 = int(x + w / 2)
    y2 = int(y + h / 2)

    # Clip boxes to stay within image
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(original_width, x2), min(original_height, y2)

    class_id = int(cls)
    class_label = class_names[class_id] if class_id < len(class_names) else f"Class {class_id}"
    label = f"{class_label}: {conf:.2f}"

    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, label, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Show result
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
