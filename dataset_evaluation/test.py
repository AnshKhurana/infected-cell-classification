import json
import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":
    with open("../data/malaria/malaria/test.json", 'rU') as fIn:
        data = json.load(fIn)
    categories = ['red blood cell', 'trophozoite', 'ring', 'schizont', 'difficult', 'gametocyte']
    with open('classes.json', 'r') as fIn:
        categories = json.load(fIn)
    print(categories)
    image = data[0]
    image_name = image['image']['pathname']
    print("Working on image " + image_name)
    im_path = '../data/malaria/malaria'  + image_name
    print(im_path)
    im_mat = cv2.imread(im_path)
    plt.imshow(im_mat)
    plt.show()
    for object in image['objects']:
        bb = object['bounding_box']
        bb_min = bb['minimum']
        bb_max = bb['maximum']
        r_min = bb_min['r']
        c_min = bb_min['c']
        r_max = bb_max['r']
        c_max = bb_max['c']
        cat = object['category']
        if cat == 'red blood cell':
            cv2.rectangle(im_mat, (r_min, c_min), (r_max, c_max), (255, 0, 0), 3)
        elif cat == 'trophozite':
            pass
        elif cat == 'ring':
            pass
        elif cat == 'schizont':
            pass
        elif cat == 'difficult':
            pass
        else:
            pass
    plt.imshow(im_mat)
    plt.show()