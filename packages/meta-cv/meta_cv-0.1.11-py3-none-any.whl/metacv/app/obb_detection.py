import numpy as np
from ..utils import preprocess, postprocess, xywhr2xyxyxyxy, xyxy2xywh


class ObbDetection:
    def __init__(self,
                 model_path: str,
                 input_width: int,
                 input_height: int,
                 use_preprocess=True,
                 pad=None,
                 normal=None,
                 mean=None,
                 std=None,
                 swap=None,
                 confidence_thresh=None,
                 nms_thresh=None,
                 class_names=None):
        self.model_path = model_path
        self.input_width = input_width
        self.input_height = input_height
        self.use_preprocess = use_preprocess
        self.pad = pad
        self.normal = normal
        self.mean = mean
        self.std = std
        self.swap = swap
        self.confidence_thresh = confidence_thresh
        self.nms_thresh = nms_thresh
        self.class_names = class_names
        self.model = None
        self.det_output = None

    def initialize_model(self):
        # todo 该函数由子类实现
        pass

    def infer(self, image):
        # todo 该函数由子类实现
        # self.outputs:
        # det_output: [1, 4 + 80, 6300]
        pass

    def predict(self, image):
        total_dets, total_scores, total_labels = [], [], []
        if isinstance(image, list):
            batch_size = len(image)
            if self.use_preprocess:
                outputs = [preprocess(im, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                      self.std, self.swap) for im in image]
                img, ratio = [out[0] for out in outputs], outputs[0][1]
            else:
                img, ratio = image, 1.0
        else:
            batch_size = 1
            if self.use_preprocess:
                img, ratio = preprocess(image, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                        self.std, self.swap)
            else:
                img, ratio = image, 1.0

        self.infer(img)
        assert self.det_output.shape[1] == (4 + len(self.class_names) + 1), "infer det output shape is not match"

        for i in range(batch_size):
            dets, det_scores, det_labels = [], [], []
            boxes = postprocess(self.det_output[i].T, score_thr=self.confidence_thresh, nms_thr=self.nms_thresh,
                                num_classes=len(self.class_names))
            if boxes is None:
                total_dets.append(dets)
                total_scores.append(det_scores)
                total_labels.append(det_labels)
                continue

            points = xywhr2xyxyxyxy(np.concatenate([xyxy2xywh(boxes[:, :4]), boxes[:, 6:]], 1))
            for pts, score, label in zip(points[:, :], boxes[:, 4], boxes[:, 5]):
                dets.append([(int(p[0] / ratio), int(p[1] / ratio)) for p in pts])
                det_scores.append(float(score))
                det_labels.append(int(label))

            total_dets.append(dets)
            total_scores.append(det_scores)
            total_labels.append(det_labels)

        return total_dets, total_scores, total_labels

    def show(self, image, dets, det_scores, det_labels):
        import cv2

        if dets is None or len(dets) == 0:
            return image
        for p, score, label in zip(dets, det_scores, det_labels):
            cv2.line(image, pt1=(p[0][0], p[0][1]), pt2=(p[1][0], p[1][1]), color=(255, 255, 0), thickness=2)
            cv2.line(image, pt1=(p[1][0], p[1][1]), pt2=(p[2][0], p[2][1]), color=(255, 255, 0), thickness=2)
            cv2.line(image, pt1=(p[2][0], p[2][1]), pt2=(p[3][0], p[3][1]), color=(255, 255, 0), thickness=2)
            cv2.line(image, pt1=(p[3][0], p[3][1]), pt2=(p[0][0], p[0][1]), color=(255, 255, 0), thickness=2)
            cv2.putText(image, '%s(%.2f)' % (self.class_names[label], score),
                        ((p[0][0] + p[2][0]) // 2, (p[0][1] + p[2][1]) // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,
                        (0, 255, 0),
                        thickness=2)

        return image
