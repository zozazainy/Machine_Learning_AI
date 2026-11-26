import pandas as p
import seaborn as sns
import matplotlib.pyplot as pt

d=p.read_csv("titanic.csv")
print (d)

# categorical data
# (A) countplot

sns.countplot(d['Survived'])
print(d['Survived'].value_counts())

sns.countplot(d['Pclass'])
print(d['Pclass'].value_counts())

sns.countplot(d['Embarked'])
print(d['Embarked'].value_counts())

# (b) PieChart

sns.countplot(d['Survived'])
d["Survived"].value_counts().plot(kind="pie",autopct="%.2f")
pt.show()

#  numerical data

# (a) histogram
pt.hist(d['Age'],bins=5)
pt.show()

#  (b) DisPlot

sns.distplot(d['Age'])
pt.show()

#  (c) BoxPlot

sns.boxplot(d["Age"])
pt.show()

print (d["Age"].min())
print(d["Age"].max())
print(d["Age"].mean())
print(d['Fare'].max())

print(d["Age"].skew())

