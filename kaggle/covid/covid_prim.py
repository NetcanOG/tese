import pandas as pd
import numpy as np

df = pd.read_csv("./covid_data.csv")

print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
#df = df.dropna(subset=["Income"])

#df = df.drop(['region', 'country', 'reportingDate'], axis=1)

first_column = df.pop('DATE_DIED')
df.insert(0, 'DATE_DIED', first_column)

df['DATE_DIED'] = np.where(df['DATE_DIED'] != '9999-99-99', 0, df['DATE_DIED'])
df['DATE_DIED'] = np.where(df['DATE_DIED'] == '9999-99-99', 1, df['DATE_DIED'])

df = df.sample(frac = 1)

df.to_csv("./covid_small.csv", index=False)
