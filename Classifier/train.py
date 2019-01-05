#Importing Libraries

import numpy as np
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib
from organize_data import load_train


img_size = 32
num_channels = 3
classes = ["Normal", "Infected"]


print('Libraries Imported')

validation_size = 0.20

images, labels = load_train(img_size)

print("Data loaded.")

df = pd.DataFrame(images, dtype=np.float32)
print(df.)

x_train, x_test, y_train_v, y_test_v = train_test_split(images, labels, test_size = 0.2, random_state = 2)


print(x_train[:5, :])

print("Dataset splitted.")

rf = RandomForestClassifier()

# Fit model
rf.fit(x_train, y_test_v)

# predictions for train
y_pred_train = rf.predict(x_train)

# predictions for test
y_pred_test = rf.predict(x_test)

# training metrics
print("Training metrics:")
print(sklearn.metrics.classification_report(y_true=y_train_v, y_pred=y_pred_train))

# test data metrics
print("Test data metrics:")
print(sklearn.metrics.classification_report(y_true=y_test_v, y_pred=y_pred_test))
