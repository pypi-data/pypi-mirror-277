#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-05-13 15:48
# @Author  : Jack
# @File    : PyLabelStudio

"""
PyLabelStudio
"""


def get_real_points(ann):
    """
    get real points from annotation
    :param ann: label studio annotation
    :return: real points array
    """
    if 'original_width' not in ann or 'original_height' not in ann:
        return None
    w, h = ann['original_width'], ann['original_height']
    points = ann['value']['points']
    if points:
        return [[w * point[0] / 100.0, h * point[1] / 100.0] for point in points]
    return None


def convert_to_box(ann):
    """
    转换标注格式
    :param ann: 标注信息
    :return: [x, y, w, h]
    """
    if 'original_width' not in ann or 'original_height' not in ann:
        return None
    value = ann['value']
    w, h = ann['original_width'], ann['original_height']
    if all([key in value for key in ['x', 'y', 'width', 'height']]):
        x, y, w, h = w * value['x'] / 100.0, h * value['y'] / 100.0, w * value['width'] / 100.0, h * value['height'] / 100.0
        return [int(x), int(y), int(x + w), int(y + h)]
    return None
