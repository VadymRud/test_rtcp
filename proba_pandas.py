import pandas as pd
data = pd.read_csv("D:\\Projects\\test_rtcp\\test_kness\\guru99.csv", sep=';', header=0).values
print(data)
for dat in data:
    print(dat[1:3])
