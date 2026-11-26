import pandas  as p
import seaborn as s
import matplotlib.pyplot as pt

titanic=p.read_csv("titanic.csv")
tips = p.read_csv("tips.csv")
flight = p.read_csv("flights.csv")
iris=p.read_csv("IRIS.csv")

tips.head()

# scatterplot (numerical-numerical)
s.scatterplot(
    x=tips['total_bill'],
    y=tips['tip'],
    hue=tips['sex'],
    style=tips['smoker'],
    size=tips['size']
)
pt.show()

# barPlot(numerical - categorical)

s.barplot(
    x=titanic['Pclass'],
    y=titanic['Age'],
    hue=titanic['Sex'])
pt.show()

# boxPlot (numerical - categorical)

s.boxplot(x=titanic['Sex'],y=titanic['Age'],hue=titanic['Survived'])
pt.show()

# distplot (numerical - categorical)
# s.distplot(titanic['Age'])

s.distplot(titanic[titanic['Survived']==0]['Age'])
s.distplot(titanic[titanic['Survived']==0]['Age'])
pt.show()