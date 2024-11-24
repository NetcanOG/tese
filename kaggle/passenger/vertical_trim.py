import pandas as pd

df = pd.read_csv("./passenger_small.csv")

df = df.iloc[97411:]

df.to_csv("./passenger_vertical_trim.csv", index=False)