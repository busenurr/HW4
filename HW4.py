import pandas as pd
df=pd.read_csv("dataset.txt", sep=";", header=0)
print(df.groupby(["Company","Payment"])["Quantity"].sum())


    