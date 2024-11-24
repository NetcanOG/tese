import pandas as pd

df = pd.read_csv("./cardio_train.csv")

#print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])
df.drop(['id'], axis=1, inplace=True)


first_column = df.pop('cardio')
df.insert(0, 'cardio', first_column)

df.to_csv("./cardio_small.csv", index=False)