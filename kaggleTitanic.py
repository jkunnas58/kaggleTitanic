import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import accuracy_score

"""
Kaggle exercise for Titanic dataset

"""

df_train = pd.read_csv("train.csv")
df_test = pd.read_csv("test.csv")

sns.countplot(x='Survived', data=df_train)


#print(df_train.describe())
#print(df_test.Age.mean)