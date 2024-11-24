import pandas as pd

df = pd.read_csv("./mushroom_small.csv")

df = df.iloc[40527:]

df.to_csv("./mushroom_vertical_trim.csv", index=False)