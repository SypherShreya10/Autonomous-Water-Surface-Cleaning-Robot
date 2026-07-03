from flask import Flask, Response
import cv2
import numpy as np
from tflite_runtime.interpreter import Interpreter

app = Flask(__name__)

# Load labels
with open("/home/pi/yolo_stream/labelmap.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Load model
interpreter = Interpreter(model_path="/home/pi/yolo_stream/yolo_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']
height, width = input_shape[1], input_shape[2]

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        img = cv2.resize(frame, (width, height))
        input_data = np.expand_dims(img, axis=0).astype(np.uint8)
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        output_data = interpreter.get_tensor(output_details[0]['index'])[0]

        for det in output_data:
            if len(det) < 6:
                continue
            x, y, w, h, conf, cls = det[:6]
            if conf < 0.5:
                continue
            x1 = int((x - w / 2) * frame.shape[1] / width)
            y1 = int((y - h / 2) * frame.shape[0] / height)
            x2 = int((x + w / 2) * frame.shape[1] / width)
            y2 = int((y + h / 2) * frame.shape[0] / height)
            class_id = int(cls)
            label = class_names[class_id] if class_id < len(class_names) else f"Class {class_id}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
