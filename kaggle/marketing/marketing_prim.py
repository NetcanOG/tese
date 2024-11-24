import pandas as pd

df = pd.read_csv("./marketing_campaign.csv", sep='\t')

#print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
df = df.dropna(subset=["Income"])
df.drop(['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Dt_Customer'], axis=1, inplace=True)


first_column = df.pop('Response')
df.insert(0, 'Response', first_column)

df.to_csv("./marketing_small.csv", index=False)