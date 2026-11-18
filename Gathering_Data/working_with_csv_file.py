import pandas as p

#g=p.read_csv("mtcars.tsv", sep="\t",names=["no","name","model","range","version","sr_code","full_code_b","1","2","3","4","5","6"])
#print (d)
#print (g)
#d=p.read_csv("aug_test.csv",header=1)
#d=p.read_csv("aug_test.csv",usecols=["enrollee_id","city",])
#d=p.read_csv("aug_test.csv",usecols=["enrollee_id","city"]).squeeze=("columns")
#d=p.read_csv("aug_test.csv",skiprows=[0,3])
#d=p.read_csv("aug_test.csv",nrows=100)
#print (d)
#g=p.read_csv("zomato.csv",sep="\t",encoding="latin_1")
#h=p.read_csv("BX-Books.csv",sep=";",encoding="latin-1",escapechar="\\")
#print (h)

#l = p.read_csv("aug_test.csv")
#l['city_development_index'] = l['city_development_index'].astype(int)

#print(l['city_development_index'])
#print(l.info())

o=p.read_csv("IPL Matches 2008-2020.csv",parse_dates=["date"])

print (o)
def rename (name):
    if name == "Asad Rauf":
        return "zozazainy"
    else:
        return name

rename ("Asad Rauf")

p.read_csv("IPL Matches 2008-2020.csv",converters={"umpire1":rename,"umpire2":rename})
