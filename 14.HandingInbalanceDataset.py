# inbalanced dataset 
# dataset with an unequal class distribution 

# if we have the dataset of diabetes in which from 1000 people only 100 has the diabetes 
# and 900 are undiabetic here the class distribution is unbalance ,it cannot read this data set 
# in our ml model ,,there fore we have to process this data before training

import numpy as np
import pandas as pd 

# loading the data set 

credit_card_data=pd.read_csv("credit_data.csv")

# print(credit_card_data.head())

# distribution of the two classes

# print(credit_card_data["Class"].value_counts())

# this highly inbalance 
# 0->Legit transections 
# 1->fraudlent transaction 

# separating the legit and fraudulent transations
leget = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

# under sampling 
# build a sample dataset containing similer distbution of legit fraudulent transection
# number of fraudent transections -492

leget_sample=leget.sample(n=492)
print(leget.shape)

# concatinate 2 data frame

new_dataset = pd.concat([leget_sample,fraud],axis=0) # because of axis=0 it will add points row wise 

print(new_dataset.head())
print(new_dataset.tail())
print(new_dataset['Class'].value_counts())