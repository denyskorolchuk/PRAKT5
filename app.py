from sklearn import datasets
import numpy as np
diabetes = datasets.load_diabetes()

print(diabetes.DESCR)

import pandas as pd
from sklearn.model_selection import train_test_split

db_df = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
print(db_df.sample(5))
db_df['Progression'] = diabetes.target #new column name 'Progression'
print(db_df.sample(2))  #checking the dataset once again.

#independent variables / explanatory variables
x = db_df.drop(labels='Progression', axis=1)  #axis=1 means we drop data by column.
#dependent variable / response / target variable.
y = db_df['Progression']

#splitting the dataset into 75%-25% train-test split 
train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.25,random_state=999)
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)

#let us import the linear regression from sklearn & create instance of the model.
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

print(lm)
print(type(lm))

lm.fit(train_x, train_y)
predicted_y = lm.predict(test_x)

#let us import metrics from sklearn to evaluate the model. Refer https://scikit-learn.org/stable/modules/model_evaluation.html for more details.
from sklearn import metrics as mt

print("1) The model explains,", np.round(mt.explained_variance_score(test_y,predicted_y)*100,2),"% variance of the target w.r.t features is")
print("2) The Mean Absolute Error of model is:", np.round(mt.mean_absolute_error(test_y,predicted_y ),2))
print("3) The R-Square score of the model is " , np.round(mt.r2_score(test_y,predicted_y),2))
