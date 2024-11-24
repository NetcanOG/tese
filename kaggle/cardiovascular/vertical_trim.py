import pandas as pd

df = pd.read_csv("./cardio_small.csv")

df = df.iloc[52501:]

df.to_csv("./cardio_vertical_trim.csv", index=False)