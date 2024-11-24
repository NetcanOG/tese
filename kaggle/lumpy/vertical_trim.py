import pandas as pd

df = pd.read_csv("./lumpy_small.csv")

df = df.iloc[18603:]

df.to_csv("./lumpy_vertical_trim.csv", index=False)