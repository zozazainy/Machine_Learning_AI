import pandas  as p
import seaborn as s

titanic=p.read_csv("titanic.csv")
tips = s.load_dataset("tips.csv")
flight = s.load_dataset("flights.csv")
iris=s.load_dataset("IRIS.csv")

# scatterplot (numerical-numerical)
s.scatterplot(tips['total_bill'],tips['tip'])
