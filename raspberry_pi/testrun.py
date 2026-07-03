# # import cv2
# # import numpy as np
# # from tflite_runtime.interpreter import Interpreter

# # # Load the labels
# # with open("labelmap.txt", "r") as f:
# #     class_names = [line.strip() for line in f.readlines()]

# # # Load the TFLite YOLO model
# # interpreter = Interpreter(model_path="yolo_model.tflite")  # Make sure this matches your model file
# # interpreter.allocate_tensors()

# # input_details = interpreter.get_input_details()
# # output_details = interpreter.get_output_details()

# # # Get input size
# # input_shape = input_details[0]['shape']
# # height, width = input_shape[1], input_shape[2]

# # # Start camera
# # cap = cv2.VideoCapture(0)

# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         break

# #     # Preprocess image
# #     img = cv2.resize(frame, (width, height))
# #     input_data = np.expand_dims(img, axis=0).astype(np.uint8)

# #     # Inference
# #     interpreter.set_tensor(input_details[0]['index'], input_data)
# #     interpreter.invoke()
# #     output_data = interpreter.get_tensor(output_details[0]['index'])[0]

# #     for det in output_data:
# #         x, y, w, h, conf, cls = det
# #         if conf < 0.5:
# #             continue

# #         # Rescale box to original image size
# #         x1 = int((x - w / 2) * frame.shape[1] / width)
# #         y1 = int((y - h / 2) * frame.shape[0] / height)
# #         x2 = int((x + w / 2) * frame.shape[1] / width)
# #         y2 = int((y + h / 2) * frame.shape[0] / height)

# #         # Get class name safely
# #         class_id = int(cls)
# #         class_label = class_names[class_id] if class_id < len(class_names) else f"Class {class_id}"

# #         label = f"{class_label}: {conf:.2f}"
# #         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #         cv2.putText(frame, label, (x1, y1 - 10),
# #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# #     cv2.imshow("YOLOv5 TFLite Detection", frame)

# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np
# from tflite_runtime.interpreter import Interpreter

# with open("labelmap.txt", "r") as f:
#     class_names = [line.strip() for line in f.readlines()]

# interpreter = Interpreter(model_path="yolo_model.tflite")
# interpreter.allocate_tensors()

# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# input_shape = input_details[0]['shape']
# height, width = input_shape[1], input_shape[2]

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     img = cv2.resize(frame, (width, height))
#     input_data = np.expand_dims(img, axis=0).astype(np.uint8)

#     interpreter.set_tensor(input_details[0]['index'], input_data)
#     interpreter.invoke()
#     output_data = interpreter.get_tensor(output_details[0]['index'])[0]

#     for det in output_data:
#         if len(det) < 6:
#             continue
#         x, y, w, h, conf, cls = det[:6]
#         if conf < 0.5:
#             continue

#         x1 = int((x - w / 2) * frame.shape[1] / width)
#         y1 = int((y - h / 2) * frame.shape[0] / height)
#         x2 = int((x + w / 2) * frame.shape[1] / width)
#         y2 = int((y + h / 2) * frame.shape[0] / height)

#         class_id = int(cls)
#         class_label = class_names[class_id] if class_id < len(class_names) else f"Class {class_id}"
#         label = f"{class_label}: {conf:.2f}"
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(frame, label, (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#     cv2.imshow("YOLOv5 TFLite Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
from tflite_runtime.interpreter import Interpreter

with open("labelmap.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

interpreter = Interpreter(model_path="yolo_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape']
input_height, input_width = input_shape[1], input_shape[2]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    original_height, original_width = frame.shape[:2]
    resized_frame = cv2.resize(frame, (input_width, input_height))
    input_data = np.expand_dims(resized_frame, axis=0).astype(np.uint8)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    for det in output_data:
        if len(det) < 6:
            continue
        x, y, w, h, conf, cls = det[:6]
        if conf < 0.5:
            continue

        # Convert normalized coords to original image coords
        x = x * original_width
        y = y * original_height
        w = w * original_width
        h = h * original_height

        x1 = int(x - w / 2)
        y1 = int(y - h / 2)
        x2 = int(x + w / 2)
        y2 = int(y + h / 2)

        # Clip boxes
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(original_width, x2), min(original_height, y2)

        class_id = int(cls)
        class_label = class_names[class_id] if class_id < len(class_names) else f"Class {class_id}"
        label = f"{class_label}: {conf:.2f}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("YOLOv5 TFLite Webcam Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
