# change dataform from json to pascalVOC

import json
from xml.etree.ElementTree import Element, SubElement, ElementTree
import os

# load original file names
origin_path_dir = 'datasets/AIhub/annotations/'
origin_file_list = os.listdir(origin_path_dir)
# print(origin_file_list)

destination_path_dir = 'datasets/AIhub/annotations_pascalVOC/'
if not os.path.exists(destination_path_dir):
    os.makedirs(destination_path_dir)


# make pascalVOC format annotation files
for filename in origin_file_list:
    with open(origin_path_dir + filename) as file:
        ann = json.load(file)
    
    filename = ann["imagePath"]


    root = Element('annotation')

    SubElement(root, 'folder').text = 'images'

    SubElement(root, 'filename').text = str(filename)

    SubElement(root, 'path').text = './images/' +  filename

    source = SubElement(root, 'source')
    SubElement(source, 'database').text = 'Unknown'

    size = SubElement(root, 'size')
    SubElement(size, 'width').text = str(ann["imageWidth"])
    SubElement(size, 'height').text = str(ann["imageHeight"])
    SubElement(size, 'depth').text = '3'


    # SubElement(root, 'segmented').text = '0'
    for i in range(len(ann["shapes"])):
        obj = SubElement(root, 'object')
        SubElement(obj, 'name').text = ann["shapes"][i]["label"]

        # SubElement(obj, 'pose').text = 'Unspecified'
        # SubElement(obj, 'truncated').text = '0'

        SubElement(obj, 'difficult').text = '0'
        
        bbox = SubElement(obj, 'bndbox')
        points = ann["shapes"][i]["points"]
        xmin, ymin = ann["imageWidth"], ann["imageHeight"]
        xmax, ymax = 0, 0
        for point in points:
            xmin = min(xmin, point[0])
            ymin = min(ymin, point[1])
            xmax = max(xmax, point[0])
            ymax = max(ymax, point[1])
        SubElement(bbox, 'xmin').text = str(xmin)
        SubElement(bbox, 'ymin').text = str(ymin)
        SubElement(bbox, 'xmax').text = str(xmax)
        SubElement(bbox, 'ymax').text = str(ymax)
    

    tree = ElementTree(root)

    tree.write(destination_path_dir + filename.split(".")[0] +'.xml')