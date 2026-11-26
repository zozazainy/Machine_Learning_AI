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

s.distplot(titanic[titanic['Survived']==0]['Age'],hist=False)
s.distplot(titanic[titanic['Survived']==0]['Age'],hist=False)
pt.show()

# heatMap (categorical - categorical)
s.heatmap(p.crosstab(titanic['Pclass'],titanic['Survived']))
pt.show()
(titanic.groupby('Pclass')['Survived'].mean() * 100).plot(kind='bar')
pt.show()

print(titanic.groupby('Sex')['Survived'].mean() * 100)

# clustermap (categorical-categorical)

print (p.crosstab(titanic['SibSp'],titanic['Survived']))

s.clustermap(p.crosstab(titanic['SibSp'],titanic['Survived']))
pt.show()

# pairplot collection of scatterplot
 
s.pairplot(iris,hue='species')
pt.show()

# lineplot (numerical - numerical) sepcial case of scatterplot

new=flight.groupby('year').sum().reset_index()
s.lineplot(x=new['year'],y=new['passengers'])
pt.show()

print(flight.pivot_table(values='passengers',index='month',columns='year'))

s.heatmap(flight.pivot_table(values='passengers',index='month',columns='year'))
pt.show()

s.clustermap(flight.pivot_table(values='passengers',index='month',columns='year'))
pt.show()