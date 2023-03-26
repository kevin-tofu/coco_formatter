
# coco_formatter

## What this repository is going to solve  

This library provides easy ways of creating and handling COCO format dataset.

## How to install

### via poetry

```bash

poetry add git+https://github.com/kevin-tofu/coco_formatter.git

```

## How to use

```python

import coco_formatter

images = coco_formatter.create_image(
    id=0,
    width=300,
    height=300,
    file_name='image.jpg'
)
```

```python

annotations = coco_formatter.create_annotation_bbox(
    id=0, 
    image_id=0, 
    category_id=0, 
    area=131.13131313, 
    bbox=np.array([30.012131, 33.13131, 120.02, 333.123]), 
)

print(annotations)
# can be dump as json text file.
import json
fpath_export = "./anns.json"
with open(fpath_export, 'w') as f:
    json.dump(annotations, f, indent=2)

```

### Get default values in original coco dataset

```python

categories = coco_formatter.get_categories()
print(categories)

licenses=coco_formatter.get_licenses()
print(licenses)

```
