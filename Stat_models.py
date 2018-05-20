import pandas as pd
import os
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression


#Path to data from samples ||| Path to location.csv for speed var
path = 'data2/samples.csv' 
dataset = pd.read_csv(path)

path2 = 'data2/location.csv'
dataB = pd.read_csv(path2)

#create columns from location.csv to samples.csv
dataset['speed'] = dataB['speed']
dataset['bearing'] = dataB['bearing']

#replace all NaN values
dataset.severity.replace(np.nan, -1, inplace=True)
dataset.aggressive.replace(np.nan, -1, inplace=True)
dataset.speed.replace(np.nan, -1, inplace=True)
dataset.bearing.replace(np.nan, -1, inplace=True)

dataset = dataset.drop('direction', axis=1)
dataset = dataset.drop('provider', axis=1)
dataset = dataset.drop('timestamp', axis=1)
dataset = dataset.drop('turn_id', axis=1)

#drop 'speed' column to make it target variable
#assign dependent and independent variables
predicators =['aggressive','severity','bearing']
one_hot_encoded_training_predictors = pd.get_dummies(predicators)

y = dataset.speed
X = dataset[predicators]



def linearRegression(x, y):
    # Split X and y into X_
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)

    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)

    for idx, col_name in enumerate(X_train.columns):
        print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0]))

    intercept = regression_model.intercept_
    print("The intercept for our model is {}".format(intercept))

    result = regression_model.score(X_test, y_test)

    return result


def decisionTree(x, y):
    model = DecisionTreeRegressor()
    model.fit(x,y)

    print(" making predictions for the following 5 houses:")
    print(x.head())
    print ("The prediction are")
    print(model.predict(x.head()))

    pred_speed = model.predict(x)
    mean_absolute_error(y,pred_speed)



    

linearRegression(X, y)
decisionTree(X, y)