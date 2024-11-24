import pandas as pd

df = pd.read_csv("./UCI_Credit_Card.csv")

print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])

df = df.drop(['ID'], axis=1)

first_column = df.pop('default.payment.next.month')
df.insert(0, 'default.payment.next.month', first_column)

df = df.sample(frac = 1)

df.to_csv("./credit_small.csv", index=False)
