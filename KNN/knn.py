import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head())

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boots = le.fit_transform(list(data["lug_boots"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"
# zipping our x data into tuples of atributes
x = list(zip(buying, maint, door, persons, lug_boots, safety))
print(x)
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# Setting up KNN model with K as 5
model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)

acc = model.score(x_test, y_test)
print(acc)

predictions = model.predict(x_test)
names = ['unacc', 'acc', 'good', 'vgood']
#for a in range(30):
#    print("prediction:{}, {} {}".format(names[predictions[a]], x_test[a], y_test[a]))

for a in range(30):
    print(model.kneighbors_graph([x_test[a]], 5))