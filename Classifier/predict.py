#Importing Libraries

import numpy as np
import pickle
import sklearn
import cv2
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier

image_size = 32
patch_width = 65
colours = [(0, 255, 0), (255, 0, 0)]

cur_model = "Models/No_adjustments_32*3_500.sav"
cur_image = "test.png"


if __name__ == '__main__':
    # filename = input("Path of model to be used: ")
    # pred_path = input("Enter path of the image: ")
    # target_name  = input("Enter path of the reference image: ")
    filename = cur_model
    pred_path = cur_image
    image = cv2.imread(pred_path)

    range_y, range_x, channels = image.shape
    disp_image = cv2.imread(pred_path)
    # disp_image = disp_image[55:-54, 55:-54]
    obj_images = []
    loaded_model = pickle.load(open(filename, 'rb'))
    debug = 0
    for itx in range(range_x):
        for ity in range(range_y):
            x_min = itx - patch_width
            x_max = itx + patch_width
            y_min = ity - patch_width
            y_max = ity + patch_width

            if x_min > 1 and x_max < range_x - 2 and y_min > 0 and y_max < range_y - 2:
                obj_image = image[y_min:y_max, x_min:x_max]
                obj_image = cv2.resize(obj_image, (image_size, image_size), 0, 0, cv2.INTER_LINEAR)
                obj_image = obj_image.astype(np.float32)
                obj_image = np.multiply(obj_image, 1.0 / 255.0)
                obj_image = obj_image.flatten()
                label = loaded_model.predict(obj_image.reshape(1, -1))
                print(itx)
                if debug == 0:
                    print(label)
                    print(disp_image.shape)
                    print(image.shape)
                    print(channels)
                    debug = 1
                disp_image[ity, itx] = colours[int(label[0])]
            else:
                pass
    plt.imshow(disp_image)
    plt.show()
