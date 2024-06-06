# WRITER: LauNT # DATE: 05/2024
# FROM: akaOCR Team - QAI

import cv2
import numpy as np
import pyclipper

from shapely.geometry import Polygon


class DetPostProcess(object):
    # The post process for Differentiable Binarization (DB).

    def __init__(self,
                 thresh         = 0.25,
                 box_thresh     = 0.5,
                 max_candidates = 1000,
                 unclip_ratio   = 1.5,
                 use_dilation   = False,
                 **kwargs):
        self.thresh = thresh
        self.box_thresh = box_thresh
        self.max_candidates = max_candidates
        self.unclip_ratio = unclip_ratio
        self.min_size = 3

    def boxes_from_bitmap(self, pred, _bitmap, dest_width, dest_height):
        # _bitmap: single map with shape (1, H, W), whose values are binarized as {0, 1}

        bitmap = _bitmap
        height, width = bitmap.shape

        contours = cv2.findContours((bitmap * 255).astype(np.uint8), cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)[0]
        num_contours = min(len(contours), self.max_candidates)
        boxes = []

        for index in range(num_contours):
            contour = contours[index]
            
            points, sside = self.get_mini_boxes(contour)
            if sside < self.min_size:
                continue

            points = np.array(points)
            score = self.box_score(pred, contour)
            if self.box_thresh > score:
                continue

            box = self.unclip(points, self.unclip_ratio).reshape(-1, 1, 2)
            box, sside = self.get_mini_boxes(box)
            if sside < self.min_size + 2:
                continue
            box = np.array(box)

            box[:, 0] = np.clip(
                np.round(box[:, 0] / width * dest_width), 0, dest_width)
            box[:, 1] = np.clip(
                np.round(box[:, 1] / height * dest_height), 0, dest_height)
            boxes.append(box.astype("int32"))

        return np.array(boxes, dtype="int32")


    def unclip(self, box, unclip_ratio):
        # Unclip a box with unclip ratio

        poly = Polygon(box)
        distance = poly.area * unclip_ratio / poly.length
        offset = pyclipper.PyclipperOffset()
        offset.AddPath(box, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)
        expanded = np.array(offset.Execute(distance))

        return expanded


    def get_mini_boxes(self, contour):
        # Get minimum boxes from contour

        bounding_box = cv2.minAreaRect(contour)
        points = sorted(list(cv2.boxPoints(bounding_box)), key=lambda x: x[0])

        index_1, index_2, index_3, index_4 = 0, 1, 2, 3
        if points[1][1] > points[0][1]:
            index_1 = 0
            index_4 = 1
        else:
            index_1 = 1
            index_4 = 0
        if points[3][1] > points[2][1]:
            index_2 = 2
            index_3 = 3
        else:
            index_2 = 3
            index_3 = 2
        box = [
            points[index_1], points[index_2], points[index_3], points[index_4]
        ]
        return box, min(bounding_box[1])


    def box_score(self, bitmap, contour):
        # box_score: use polyon mean score as the mean score

        h, w = bitmap.shape[:2]
        contour = contour.copy()
        contour = np.reshape(contour, (-1, 2))

        xmin = np.clip(np.min(contour[:, 0]), 0, w - 1)
        xmax = np.clip(np.max(contour[:, 0]), 0, w - 1)
        ymin = np.clip(np.min(contour[:, 1]), 0, h - 1)
        ymax = np.clip(np.max(contour[:, 1]), 0, h - 1)

        mask = np.zeros((ymax - ymin + 1, xmax - xmin + 1), dtype=np.uint8)

        contour[:, 0] = contour[:, 0] - xmin
        contour[:, 1] = contour[:, 1] - ymin
        cv2.fillPoly(mask, contour.reshape(1, -1, 2).astype("int32"), 1)

        return cv2.mean(bitmap[ymin:ymax + 1, xmin:xmax + 1], mask)[0]


    def __call__(self, outs_dict, shape_list):
        # The post process to get bounding boxes

        # get mask from pred
        pred = outs_dict['maps']
        pred = pred[:, 0, :, :]
        segmentation = pred > self.thresh
        src_h, src_w = shape_list[0][0:2]
        mask = segmentation[0]

        # get box from mask
        boxes = self.boxes_from_bitmap(pred[0], mask, src_w, src_h)

        return boxes