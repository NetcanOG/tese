import pandas as pd

FILENAME = "passenger_vertical_trim"
name = "passenger"
two_cut_off = 8 
three_cut_off = 12
max = 23
two_to_remove = []
three_to_remove = []

while two_cut_off < max:
    two_to_remove.append(two_cut_off)
    two_cut_off += 1
print("two_to_remove")
print(two_to_remove)

while three_cut_off < max:
    three_to_remove.append(three_cut_off)
    three_cut_off += 1
print("three_to_remove")
print(three_to_remove)

df = pd.read_csv("./"+FILENAME+".csv")

df2 = df.drop(df.columns[two_to_remove], axis=1)
df3 = df.drop(df.columns[three_to_remove], axis=1)

df2.to_csv("./"+name+"_2.csv", index=False)
df3.to_csv("./"+name+"_3.csv", index=False)