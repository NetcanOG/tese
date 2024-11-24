import pandas as pd

df = pd.read_csv("./lumpy_vertical_trim.csv")
split_value = 8

d1 = df.iloc[:, :split_value]
d2 = df.iloc[:, split_value:]

binary = df.iloc[:, :1]
d2.insert(0, binary.columns[0], binary.values)

print(d1.iloc[:0])
print(d2.iloc[:0])
print(d2)

d1.to_csv("./data_split1.csv", index=False)
d2.to_csv("./data_split2.csv", index=False)