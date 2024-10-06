# data standardization 

# a process of standardizing the data to a common format and common range

import numpy as np 
import pandas as pd 
import sklearn.datasets # this will give some sample data sets
from sklearn.preprocessing import StandardScaler # this is a function used to standard our data set
from sklearn.model_selection import train_test_split # this will split the data in training testing data 

# loading the data set 
dataset = sklearn.datasets.load_breast_cancer()
# print(dataset)
# in this data set we have to predict weather the person has cancer or not 
# ,,,here 0 represents the benign stage(beging) and 1 means advance stage

# loading the data into pandas dataframe
df=pd.DataFrame(dataset.data,columns=dataset.feature_names)
# print(df.head())

x=df # this represents the features
y=dataset.target # this has the result weather the person has cancer or not

# print(x)
# print(y)

# spliting the data into training and test data 

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.2,random_state=3)

# print(y_test)
# print(y_train)

# standaridize the data

print(dataset.data.std())#if data is in the same range the std should be 1

scaler=StandardScaler() # this function will apply the formula z=(x-u)/s ,, here x is a datapoint
                        # u is the mean of x  and s represents th standard deviation of x 
                        # this formula will change the value of the range but ,dose'nt affect the 
                        # nature of the data 
        
scaler.fit(x_train) # this function will analize and ubnderstand ,,how the data is distributed  

# now we have to transform this data based on standerd scaler
x_train_standardized=scaler.transform(x_train)

x_test_standardized=scaler.transform(x_test)

print(x_train_standardized.std())