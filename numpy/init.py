import pandas as pd
import json
import csv 

df = pd.read_csv("test.csv")

df.drop_duplicates()

print(df.to_dict(orient="records"))
