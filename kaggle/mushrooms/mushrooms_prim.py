import pandas as pd

df = pd.read_csv("./mushroom_cleaned.csv")

#print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])
#df.drop(['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Dt_Customer'], axis=1, inplace=True)


first_column = df.pop('class')
df.insert(0, 'class', first_column)

df = df.sample(frac=1)

df.to_csv("./mushroom_small.csv", index=False)