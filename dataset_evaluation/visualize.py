import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("../malaria/malaria/test.json", 'rU') as fIn:
        data = json.load(fIn)
        count = 0
        num_cat = 0
        categories = []
        with open('classes.json', 'r') as fIn:
            categories = json.load(fIn)
        print(categories)
        image = data[0]
        print("Working on image " + image['image']['pathname'])
        for object in image['objects']:
            bb = object['bounding']
