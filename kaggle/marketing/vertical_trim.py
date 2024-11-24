import pandas as pd

df = pd.read_csv("./marketing_small.csv")

df = df.iloc[1663:]

df.to_csv("./marketing_vertical_trim.csv", index=False)