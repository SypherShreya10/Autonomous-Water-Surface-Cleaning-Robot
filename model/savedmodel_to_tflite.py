import tensorflow as tf

# Load the SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("yolo_saved_model")

# ✅ Enable fallback to TensorFlow ops
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,  # allow TFLite ops
    tf.lite.OpsSet.SELECT_TF_OPS     # allow select TF ops like SplitV
]

# Optional: reduce model size (skip this if it causes errors)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert the model
tflite_model = converter.convert()

# Save the model
with open("yolo_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Model converted to TFLite with TF Select fallback enabled.")
