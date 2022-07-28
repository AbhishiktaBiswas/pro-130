import csv
import pandas as pd

df=pd.read_csv("total_stars.csv")
print(df.shape)

del df["Star_name"]
del df["Luminosity"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv('main.csv')