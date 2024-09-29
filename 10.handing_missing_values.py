# how to handle missing values in dataset
# 
# methods to handle missing values:

#   1.imputation
#       using some proper statical values and replacing missing 
#       values to those staticial values(mean, median, mode)AKA centrial tendencies
#           1)mean=the avarage of all the values
#           2)median = arrange all the values in assanding and then we will take the middle
#                       value ,, this represent's the median ,,and if there are two middle value's
#                       then take the avarage of those two values
#           3)mode = the mode is the number which has the most frequency
#   2.Dropping
#       It is deleting all the rows that have the missing values,
#       this is not a efficent way when we have a smaller data set

# we cannot feed our dataset with the missing values,,therefore 
# we have to replace all those missing values before feeding

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading a csv file 

dataset=pd.read_csv('/home/shubham/Videos/ML_pra/Placement_Data_Full_Class.csv')

# print(dataset.head())
# print(dataset.isnull().sum())# this function gives the number of missin values for all the columns

# understanding when to use which centerial tendancies
# analyse the distribution of data in the missing coloum (salary coloum)


# fig, ax = plt.subplots(figsize=(8,8))
# sns.displot(dataset.salary)
# plt.show()


# in this data set the data is destributed is only in one side/area (eg. here betweet 2-4)
# but we have some out layer's ,,this kind of curve is known as 'skew'
# in these cases we cannot use mean values because when you have these out layers these 
# can increase your mean value
# in this case we can replace the value with median or mode 
# when the data is distributed normally then we can use mean

# replacing the missing value with median value

dataset['salary'].fillna(dataset['salary'].median(),inplace=True) # this will replace all the 
                                                                  # missing values with median

print(dataset.isnull().sum()) 

# droping method 
salary_dataset=pd.read_csv('/home/shubham/Videos/ML_pra/Placement_Data_Full_Class.csv')
print(salary_dataset.shape)
print(salary_dataset.isnull().sum())

# now we want to drop all the rows with missing values

salary_dataset=salary_dataset.dropna(how='any')
print(salary_dataset.shape)
print(salary_dataset.isnull().sum())

