import pandas as pd
import numpy as np
#import FirstTF
#import keras
#from keras.models import load_model
import sklearn
from sklearn import linear_model
#from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

# Reading the csv with panda, since data is separated by semicolon we specify delimiter ';'
data = pd.read_csv("./student-mat.csv", sep=';')

# Specifying the attributes we want to see
data = data[['G1', 'G2', 'G3', 'studytime', 'absences', 'failures']]

# Gotta specify a label, which is what we will attempt to predict with our linear regression ML
predict = "G3"

# creating data frame x and y, x is the attributes that will be used to predict dataframe y
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

''' splitting our x and y arrays into 4 arrays which will be a training arrays and our test arrays, 
our test array's sizes will be 10% of our actual data because it would be dumb for the testing arrays to already have all the data.
https://www.youtube.com/watch?v=1BYu65vLKdA
'''
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

bestAcc = 0
for a in range(300):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

    # creating linear model - imagine this like creating a line on the plane, not fitted to anything but a line is made.
    linear = linear_model.LinearRegression()
    # fitting our lines to our training data. acc is the accuracy of our linear regression algorithm. We test it with linear.score method
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    if acc > bestAcc:
        bestAcc = acc
        # saving our model to a pickle file
        with open('./studentmodel.pickle', 'wb') as f:
            pickle.dump(linear, f)
        print(acc)

    # opening it, make sure to close later!
with open('./studentmodel.pickle', "rb") as f:
    linear = pickle.load(f)


# going to show the coefficients and intercepts of model (remember y=mx+b example?)
print('co: {}'.format(linear.coef_))
print('intercepts: {}'.format(linear.intercept_))
# You can see in the coeficient, the bigger the slope/coefficient the bigger the weight is has on the prediction

predictions = linear.predict(x_test)

# print out what the compputer predicted, the attributes, then the actual mark they got
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = "G1"
p2 = "G2"
style.use('fivethirtyeight')
pyplot.scatter(data[p], data[predict])
pyplot.scatter(data[p2], data[predict], color="g")
pyplot.xlabel("Initial Grades")
pyplot.ylabel("final grade")
pyplot.xticks(np.arange(1,20,0.5))
pyplot.show()