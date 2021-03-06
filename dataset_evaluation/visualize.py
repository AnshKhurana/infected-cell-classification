import json
import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":
    with open("../data/malaria/malaria/training.json", 'rU') as fIn:
        data = json.load(fIn)
    # categories = ['red blood cell', 'trophozoite', 'ring', 'schizont', 'difficult', 'gametocyte']
    with open('classes.json', 'r') as fIn:
        categories = json.load(fIn)
    print(categories)
    image = data[0]
    image_name = image['image']['pathname']
    print("Working on image " + image_name)
    im_path = '../data/malaria/malaria' + image_name
    print(im_path)
    im_mat = cv2.imread(im_path)
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
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (255, 0, 0), 3)
        elif cat == 'trophozite':
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (0, 0, 255), 3)
        elif cat == 'ring':
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (255, 255, 0), 3)
        elif cat == 'schizont':
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (255, 128, 0), 3)
        elif cat == 'difficult':
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (0, 0, 0), 3)
        else:
            cv2.rectangle(im_mat, (c_min, r_min), (c_max, r_max), (128, 64, 128), 3)
    plt.imshow(im_mat)
    plt.show()
    plt.imsave('sample_image', im_mat)