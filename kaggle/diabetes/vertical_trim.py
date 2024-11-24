import pandas as pd

df = pd.read_csv("./diabetes.csv")

df = df.iloc[577:]

df.to_csv("./diabetes_vertical_trim.csv", index=False)