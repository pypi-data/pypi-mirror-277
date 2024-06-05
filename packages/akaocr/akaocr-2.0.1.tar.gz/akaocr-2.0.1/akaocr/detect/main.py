# WRITER: LauNT # DATE: 05/2024
# FROM: akaOCR Team - QAI

import numpy as np
import os
import traceback

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

from akaocr.detect.center.engines import create_predictor
from akaocr.detect.center.engines import build_post_process
from akaocr.detect.center.data import create_operators
from akaocr.detect.center.data import transform


class Detector(object):
    def __init__(self, model_path=None, side_len=736, conf_thres=0.5):
        # Init some parameters

        pre_process_list = [ # build pre-procesing
            {'DetResize': {'limit_side_len': side_len, 'limit_type': 'min'}}, 
            {'NormalizeImage': 
                {
                    'std': [0.229, 0.224, 0.225],
                    'mean': [0.485, 0.456, 0.406],
                    'scale': '1./255.', 'order': 'hwc'
                }
            },
            {'ToCHWImage': None}, {'KeepKeys': {'keep_keys': ['image', 'shape']}}
        ]
        self.preprocess_op = create_operators(pre_process_list)
        
        self.conf_thres = conf_thres
        self.output_tensors = None
        
        # build post-processing
        postprocess_params = {}
        postprocess_params['name']           = 'DetPostProcess'
        postprocess_params["thresh"]         = 0.4
        postprocess_params["box_thresh"]     = self.conf_thres
        postprocess_params["max_candidates"] = 1000
        postprocess_params["unclip_ratio"]   = 2.0
        postprocess_params["use_dilation"]   = False
        self.postprocess_op = build_post_process(postprocess_params)

        # create predictor
        self.predictor, self.input_tensor = create_predictor(model_path)


    def order_points_clockwise(self, pts):
        # Order points clockwise

        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        tmp = np.delete(pts, (np.argmin(s), np.argmax(s)), axis=0)
        diff = np.diff(np.array(tmp), axis=1)
        rect[1] = tmp[np.argmin(diff)]
        rect[3] = tmp[np.argmax(diff)]

        return rect


    def clip_det_res(self, points, img_height, img_width):
        # Clip detection results

        for pno in range(points.shape[0]):
            points[pno, 0] = int(min(max(points[pno, 0], 0), img_width - 1))
            points[pno, 1] = int(min(max(points[pno, 1], 0), img_height - 1))

        return points


    def filter_det_res(self, dt_boxes, image_shape):
        # Filter tag detection results

        img_height, img_width = image_shape[0:2]
        dt_boxes_new = []

        for box in dt_boxes:
            box = self.order_points_clockwise(box)
            box = self.clip_det_res(box, img_height, img_width)

            rect_width = int(np.linalg.norm(box[0] - box[1]))
            rect_height = int(np.linalg.norm(box[0] - box[3]))
            if rect_width <= 3 or rect_height <= 3:
                continue
            dt_boxes_new.append(box.astype(int).tolist())

        return dt_boxes_new


    def __call__(self, ori_image):
        # Inference for text detection

        image = ori_image.copy()
        data = {'image': image}

        # transform image
        image, shape_list = transform(data, self.preprocess_op)
        image = np.expand_dims(image, axis=0)
        shape_list = np.expand_dims(shape_list, axis=0)

        # inference model
        input_dict = {}
        input_dict[self.input_tensor.name] = image
        outputs = self.predictor.run(self.output_tensors, input_dict)
       
        # post-processing
        preds = dict()
        preds['maps'] = outputs[0]
        dt_boxes = self.postprocess_op(preds, shape_list)
        dt_boxes = self.filter_det_res(dt_boxes, ori_image.shape)
      
        return dt_boxes


class BoxEngine():
    def __init__(self, model_path=None, side_len=736, conf_thres=0.5):
        # Init some parameters

        self.text_detector = Detector(model_path, side_len, conf_thres)

    def __call__(self, image):
        # Text Detection Pipeline
        
        det_res = None
        try:
            det_res = self.text_detector(image)
        except Exception:
            print(traceback.format_exc())

        return det_res