
from typing import Optional, Tuple, List, Union
import numpy as np

def create_image(
    id: int, 
    width: int, 
    height: int, 
    file_name: str, 
    license: Optional[int], 
    flickr_url: Optional[str], 
    coco_url: Optional[str], 
    date_captured: Optional[Union[str, datetime]]
):
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
        ret['date_captured'] = date_captured if type(date_captured) is str
    
    return ret

def create_annotation_bbox(
    id: int, 
    image_id: int, 
    category_id: int, 
    area: float, 
    bbox: Union[List[float], np.ndarray], 
    segmentation: Optional[List[List[float]]], 
    iscrowd: Optional[int],
):
    
    iscrowd = 0 if iscrowd is None else iscrowd
    if type(bbox) is np.ndarray:
        bbox = bbox.tolist()
        
    ret = dict(
        id = id, 
        image_id = image_id, 
        category_id = category_id, 
        area = area, 
        bbox = bbox, 
        iscrowd = ret
    )

    if segmentation is not None:
        ret['segmentation'] = segmentation


    return ret
