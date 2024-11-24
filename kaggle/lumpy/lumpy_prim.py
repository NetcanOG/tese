import pandas as pd

df = pd.read_csv("./Lumpy_skin_disease_data.csv")

print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])

df = df.drop(['region', 'country', 'reportingDate'], axis=1)

first_column = df.pop('lumpy')
df.insert(0, 'lumpy', first_column)

df = df.sample(frac = 1)

df.to_csv("./lumpy_small.csv", index=False)
