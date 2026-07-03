from onnx_tf.backend import prepare
import onnx

model = onnx.load("best.onnx")
tf_rep = prepare(model)
tf_rep.export_graph("yolo_saved_model")
