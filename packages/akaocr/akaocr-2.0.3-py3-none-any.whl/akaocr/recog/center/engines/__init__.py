# WRITER: LauNT # DATE: 05/2024
# FROM: akaOCR Team - QAI

import onnxruntime as ort
import os
import copy

from .engine import CTCLabelDecode
from .utility import resize_image


__all__ = ['build_post_process', 'create_predictor', 'resize_image']


def build_post_process(config, global_config=None):
    # Post-processing for recognition model

    support_dict = [
        'CTCLabelDecode'
    ]
    config = copy.deepcopy(config)
    module_name = config.pop('name')

    if global_config is not None:
        config.update(global_config)
    assert module_name in support_dict, Exception(
        'post process only support {}'.format(support_dict))
    module_class = eval(module_name)(**config)

    return module_class


def create_predictor(model_path):
    # Create predictor for model inference phase

    work_dir = os.path.dirname(os.path.realpath(__file__))
    providers = ['CUDAExecutionProvider','CPUExecutionProvider']

    if not model_path:
        model_path = "data/model.onnx"
        rec_model_path = os.path.join(work_dir, "../../", model_path)
    else:
        rec_model_path = model_path
    sess = ort.InferenceSession(rec_model_path, providers=providers)
    
    return sess, sess.get_inputs()[0], None