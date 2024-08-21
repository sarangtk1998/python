


import pandas as pd

df = pd.read_csv('weatherData.csv',names=['outlook','temprature','humidity','windy','play'])

print(df.head())

print('*'*100)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()



print(df.head())



