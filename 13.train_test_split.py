# ML project 
'''
1)data
= collect the raw data to train the model 
2)data pre processing
= handel some missing values or standradized the data 
3)data analysis
= figering out which data (features) is important for our preduction 
4)train test split 
= in this we split the oriaginal data in test and training data
5)machine learning model 
= we will feed this data to our ml model  
6)evaluation 
= this evalution will be based on the test data,,finding how the model is performing
    and the accuracy score of the model
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm # support vector machine model for training 
from sklearn.metrics import accuracy_score

dib_db=pd.read_csv('diabetes.csv')
# print(dib_db)

print(dib_db['Outcome'].value_counts())

# storing all the features in x and labels/outcomes in y
X = dib_db.drop(columns='Outcome',axis=1)
Y = dib_db['Outcome']
# print(X)
# print(Y)

# standredization of data
scaler=StandardScaler()
scaler.fit(X)
standredized_data=scaler.transform(X)
print(standredized_data)

X=standredized_data

# splitting the data into training data and testing data

# create 4 arrays
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=2)