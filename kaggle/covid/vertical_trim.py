import pandas as pd

df = pd.read_csv("./covid_small.csv")

df = df.iloc[786432:]

df.to_csv("./covid_vertical_trim.csv", index=False)