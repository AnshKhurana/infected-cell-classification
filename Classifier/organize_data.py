import json
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

img_size = 64
num_channels = 3
classes = ["Normal", "Infected"]
def load_train(image_size, classes):
    images = []
    labels = []
    # img_names = []
    # cls = []
    debug = True
    print('Going to read training images')
    with open("../data/malaria/malaria/training.json", 'rU') as fIn:
        training_data = json.load(fIn)
    for img in training_data:
        image_data = img["image"]
        objects = img["objects"]
        image_path = image_data["pathname"]
        image_path = '../data/malaria/malaria' + image_path
        print(image_path)
        image = cv2.imread(image_path)
        for obj in objects:
            bb = obj['bounding_box']
            bb_min = bb['minimum']
            bb_max = bb['maximum']
            r_min = bb_min['r']
            c_min = bb_min['c']
            r_max = bb_max['r']
            c_max = bb_max['c']
            cat = obj['category']
            obj_image = image[r_min:r_max, c_min:c_max]
            obj_image = cv2.resize(obj_image, (image_size, image_size),0,0, cv2.INTER_LINEAR)
            obj_image = obj_image.astype(np.float32)
            obj_image = np.multiply(obj_image, 1.0 / 255.0)
            images.append(obj_image)

            if cat == "red blood cell":
                label = classes[0]
            else:
                label = classes[1]

            labels.append(label)
            if debug:
                plt.imshow(obj_image)
                plt.show()
                print(label)
                debug = False
            # flbase = os.path.basename(fl)
            # img_names.append(flbase)
            # cls.append(fields)
    images = np.array(images)
    labels = np.array(labels)
    # img_names = np.array(img_names)
    # cls = np.array(cls)
    return images, labels

def read_data():
    load_train(img_size, classes)


if __name__ == '__main__':
    images, labels = load_train(img_size, classes)
    print(images.size, labels.size)
    # os.chdir("~/Desktop/infected-cell-classification")