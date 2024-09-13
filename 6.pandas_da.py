'''
pandas is a data processing and analysis library

pandas dataframe 
it is a two-dimensional tabular data structure with labeled axes(rows and colomns)
'''
import pandas as pd
import numpy as np
# creating a dataframe

# importing the iris house price data
from sklearn.datasets import load_iris
iris =load_iris()
iris_df=pd.DataFrame(iris.data,columns=iris.feature_names) # creating a dataframe
# print(iris_df.head())
# print(iris_df.shape)

## importing a csv file

greenhouse=pd.read_csv('/home/shubham/Downloads/greenhouse.csv')
# # print(greenhouse.head())
# print(type(greenhouse))

# loading the excel file
# pd.read_excel('file_path')

##  Exporting Dataframe into csv file
# iris_df.to_csv('iris.csv')

## creating a random dataframe
# random_df=pd.DataFrame(np.random.rand(20,10))
# print(random_df)

## inspecting a dataframe 

# first 5 rows in the dataframe
# print(iris_df.head())

# # last 5 rows in the dataframe
# print(iris_df.tail())

# # information about the data frame
# print(iris_df.info())

# # discripshion about the data frame
# print(iris_df.describe())

# # finding the number of missing values 
# print(iris_df.isnull().sum())

# # counting the values based on the label
# print(iris_df.value_counts("sepal length (cm)"))

# # grouping the values based on the mean
# print(iris_df.groupby('sepal length (cm)').mean())

# # mean value column wise
# print(iris_df.mean())

## manipulating a dataframe

# adding column to a dataframe

iris_df['Price']=iris.target
print(iris_df.head())

# removing a row 
iris_df.drop(index=0,axis=0)
print(iris_df.head())

# drop a column 
print(iris_df.drop(columns='Price',axis=1))

# locating a row using a index value 
print(iris_df.iloc[2])

# locating a perticular column
print(iris_df.iloc[:,2]) 
print(iris_df.corr())