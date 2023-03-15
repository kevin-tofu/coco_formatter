import json

fpath = '/home/kohei/Downloads/annotations_trainval2017/annotations/instances_val2017.json'
with open(fpath, 'rb') as f:
    data = json.load(f)

print(data.keys())
print(data['categories'])
print(data['annotations'][0])