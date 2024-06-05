# WRITER: LauNT # DATE: 05/2024
# FROM: akaOCR Team - QAI

import copy
import os
import onnxruntime as ort

from .engine import DetPostProcess

__all__ = ['build_post_process', 'create_predictor']


def build_post_process(config, global_config=None):
    # Build post processing
    
    support_dict = [
        'DetPostProcess'
    ]
    config = copy.deepcopy(config)
    module_name = config.pop('name')

    if global_config is not None:
        config.update(global_config)
        
    assert module_name in support_dict, Exception(
        'Post process only support {}'.format(support_dict))
    module_class = eval(module_name)(**config)

    return module_class


def create_predictor(det_model_path):
    # Create predictor for onnx model inference

    work_dir = os.path.dirname(os.path.realpath(__file__))

    if (det_model_path is None) or (not os.path.exists(det_model_path)):
        model_path = "data/model.onnx"
        det_model_path = os.path.join(work_dir, "../../", model_path)

    providers = ['CPUExecutionProvider']
    sess = ort.InferenceSession(det_model_path, providers=providers)

    return sess, sess.get_inputs()[0]