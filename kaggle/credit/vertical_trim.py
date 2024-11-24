import pandas as pd

df = pd.read_csv("./credit_small.csv")

df = df.iloc[22501:]

df.to_csv("./credit_vertical_trim.csv", index=False)