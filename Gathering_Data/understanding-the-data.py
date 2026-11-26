import pandas as p
d=p.read_csv("train.csv")
print(d)

# understanding the data

# 1. how big the data is 
print (d.shape)

# 2. how does the data look like
print (d.head()) # give me first five rows
print (d.sample(5)) #give me random rows

# 3. what is the data type of columns
print (d.info())

# 4. are there any missing values
print (d.isnull().sum()) 

# how does the data mathematically
print (d.describe())

# are there any duplicate values
print (d.duplicated().sum())

# how is the correlation (measures how strongly two variables move together across rows in a dataset, producing a score from -1 to +1 (most commonly using Pearson's formula for linear relationships) between columns?
# print(d.corr()["AB"])
print (d.corr())

