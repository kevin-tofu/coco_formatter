#!/usr/bin/env python3
# Copyright (c) Kevin-Tofu, koheitech001@gmail.com

from typing import Optional, Union, Literal
import numpy as np
import datetime

def create_image(
    id: int, 
    width: int, 
    height: int, 
    file_name: str, 
    license: Optional[int] = None, 
    flickr_url: Optional[str] = None, 
    coco_url: Optional[str] = None, 
    date_captured: Optional[Union[str, datetime.datetime]] = None
)  -> dict:
    ret = dict(
        id = id,
        width = width,
        height = height,
        file_name = file_name
    )

    if license is not None:
        ret['license'] = license
    if flickr_url is not None:
        ret['flickr_url'] = flickr_url
    if coco_url is not None:
        ret['coco_url'] = coco_url
    if date_captured is not None:
        # 2013-11-14 17:02:52
        ret['date_captured'] = date_captured if type(date_captured) is str else str(date_captured)
    
    return ret

def create_annotation_bbox(
    id: int, 
    image_id: int, 
    category_id: int, 
    area: float, 
    bbox: Union[list[float], np.ndarray], 
    segmentation: Optional[list[list[float]]] = None, 
    iscrowd: Optional[Literal[0, 1]] = None,
    score: Optional[float] = None
) -> dict:
    
    iscrowd = 0 if iscrowd is None else iscrowd
    if type(bbox) is np.ndarray:
        bbox = bbox.tolist()

    ret = dict(
        id = id, 
        image_id = image_id, 
        category_id = category_id, 
        area = round(area, 2), 
        bbox = [round(b, 2) for b in bbox], 
        iscrowd = iscrowd
    )

    if segmentation is not None:
        ret['segmentation'] = segmentation
    if score is not None:
        ret['score'] = round(score, 2)

    return ret

def create_category(
    id: int, 
    name: str, 
    supercategory: Optional[str]
) -> dict:
    ret = dict(
        id = id, 
        name = name,
    )
    if supercategory is not None:
        ret['supercategory'] = supercategory
    return ret

def create_license(
    id: int, 
    name: str, 
    url: Optional[str] = None
) -> dict:

    ret = dict(
        id = id, 
        name = name
    )
    if url is not None:
        ret['url'] = url
    return ret