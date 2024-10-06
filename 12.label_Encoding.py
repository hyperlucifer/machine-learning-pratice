# Label Encoding
#       converting the labels into numeric form
# primery used in classification problem

import pandas as pd 
import sklearn.datasets
from sklearn.preprocessing import LabelEncoder

# label Encoding of breast cancer dataset

# load dataset to a dataframe 
cancer_data=pd.read_csv('data.csv')
# print(cancer_data.head())

# finding the count of different labels
print(cancer_data['diagnosis'].value_counts()) # this will tell us number of m,b cases

# now we are going to convert the currousponding label value into numircal data values

# load the label encoder function

Label_Encoder=LabelEncoder()
label =Label_Encoder.fit_transform(cancer_data.diagnosis)

# appending the labels to a data frame
cancer_data['target'] = label
# print(cancer_data.head())

# 0=benign
# 1=malignant

# for iris data set 

iris_dataset=pd.read_csv('Iris2.csv')
print(iris_dataset.head())
label2=Label_Encoder.fit_transform(iris_dataset.Species)

# appending new coloum
iris_dataset['target']=label2

# print(iris_dataset.head())
print(iris_dataset['target'].value_counts())

# this will alocate the number's from 0 and gives the number from alphabaticaly 
