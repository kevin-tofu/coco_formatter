# coco_formatter
## What this repository is going to solve  


##
```
pip install git+https://github.com/kevin-tofu/coco_formatter.git
```
## How to use
```
import coco_formatter

images = coco_formatter.create_image(
    id = 0,
    width = 300,
    height = 300,
    file_name = 'image.jpg'
)
```

```
annotations = coco_formatter.create_annotation_bbox(
    id = 0, 
    image_id = 0, 
    category_id = 0, 
    area = 131.13131313, 
    bbox = np.array([30.012131, 33.13131, 120.02, 333.123]), 
)

print(annotations)
```
```
categories = coco_formatter.get_categories()
print(categories)

licenses = coco_formatter.get_licenses()
print(licenses)
```
