import pandas as pd

df1 = pd.read_csv("./train.csv")
df2 = pd.read_csv("./test.csv")
frames = [df1,df2]
#print(df.shape)
dfinal = pd.concat(frames)
#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])
#df.drop(['id'], axis=1, inplace=True)

dfinal = dfinal.replace({'Male':0, 'Female':1, 'Loyal Customer':0, 'disloyal Customer':1, 'Personal Travel':0, 'Business travel':1, 'Business':0, 'Eco':1, 'Eco Plus':2, 'satisfied':0, 'neutral or dissatisfied':1})
dfinal.drop(['#','id'], axis=1, inplace=True)

first_column = dfinal.pop('satisfaction')
dfinal.insert(0, 'satisfaction', first_column)

dfinal.to_csv("./passenger_small.csv", index=False)