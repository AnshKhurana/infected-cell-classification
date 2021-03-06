import json
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from numpy.core.multiarray import ndarray
from stain_test import transform

img_size = 32
num_channels = 3
classes = ["Normal", "Infected"]
def load_train(image_size):
    # target  = input("path to target_name")
    target_path = "../data/malaria/malaria/special/standard.png"
    images = []
    labels = []
    count = 0
    num_img = 0
    avg_height = 0
    avg_width = 0
    debug = True
    print('Going to read training images')
    with open("../data/malaria/malaria/training.json", 'rU') as fIn:
        training_data = json.load(fIn)
    for img in training_data:
        count = count + 1
        if count > 600:
            break
        image_data = img["image"]
        objects = img["objects"]
        image_path = image_data["pathname"]
        image_path = '../data/malaria/malaria' + image_path
        print(image_path)
        # image = cv2.imread(image_path, 0)
        image = transform(image_path, target_path)
        for obj in objects:
            num_img = num_img + 1
            bb = obj['bounding_box']
            bb_min = bb['minimum']
            bb_max = bb['maximum']
            r_min = bb_min['r']
            c_min = bb_min['c']
            r_max = bb_max['r']
            c_max = bb_max['c']
            avg_height = avg_height + r_max - r_min
            avg_width = avg_width + c_max - c_min
            obj_image = image[r_min:r_max, c_min:c_max]
            obj_image = cv2.resize(obj_image, (image_size, image_size), 0, 0, cv2.INTER_LINEAR)
            obj_image = obj_image.astype(np.float32)
            obj_image = np.multiply(obj_image, 1.0 / 255.0)
            if debug:
                print(obj_image.shape)
                plt.imshow(obj_image)
                plt.show()

            obj_image = obj_image.flatten()
            if debug:
                print(obj_image)
                print(type(obj_image))
                print(obj_image.shape)
                debug = False
            images.append(obj_image)
            cat = obj['category']
            if cat == "red blood cell":
                label = 0
            else:
                label = 1

            labels.append(label)


    images = np.array(images)
    labels = np.array(labels)
    avg_width = avg_width/num_img
    avg_height = avg_height/num_img

    print("Average height for patch = " + str(avg_height))
    print("Average width for patch = " + str(avg_width))
    return images, labels

def read_data():
    load_train(img_size)

if __name__ == '__main__':
    images, labels = load_train(img_size)
    print(images.shape, labels.shape)
    # np.savetxt("images.csv", images.flatten())
    # np.savetxt("labels.csv", labels)
    print("organization completed")
    # os.chdir("~/Desktop/infected-cell-classification")