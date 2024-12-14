# importing dependencies
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Data collection and pre-processing

# loading data

diabetes_data=pd.read_csv("diabetes.csv")
print(diabetes_data.head())
print(diabetes_data.shape)
print(diabetes_data.describe())

# seprating features and target

X=diabetes_data.drop(columns='Outcome',axis=1)
Y=diabetes_data['Outcome']

print(X)
print(Y)

# Data standarization 

scaler =StandardScaler()
Standardized_data= scaler.fit_transform(X)
print(Standardized_data)
X=Standardized_data


# Spliting the data into training and testing data 

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

# now we can feed this data to our machine learning module
