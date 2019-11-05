


import pandas as pd
df=pd.read_csv("dataset.txt", sep=";", header=0)
print(df.groupby(["Company","Payment"])["Quantity"].sum())
companies = {"Deloite & Touche": {"Cash": 0, "Credit": 0},
            "EY": {"Cash": 0, "Credit": 0},
            "KPMG": {"Cash": 0, "Credit": 0},
            "PWC": {"Cash": 0, "Credit": 0}}
for i in range(len(df)):
    companylist, payment, quantity = df.iloc[i]["Company"], df.iloc[i]["Payment"], df.iloc[i]["Quantity"]
    companies[companylist][payment] = quantity  
for key,value in companies.items():
    companylist= key
    cash = value["Cash"]
    credit= value["Credit"]
    print("From {0} {1} people have bought stuff on discount and paid in cash, also assistants got {2} serving of coffee on credit".format(companylist,cash,credit))
    





