import pandas as p

#g=p.read_csv("mtcars.tsv", sep="\t",names=["no","name","model","range","version","sr_code","full_code_b","1","2","3","4","5","6"])
#print (d)
#print (g)
#d=p.read_csv("aug_test.csv",header=1)
#d=p.read_csv("aug_test.csv",usecols=["enrollee_id","city",])
#d=p.read_csv("aug_test.csv",usecols=["enrollee_id","city"]).squeeze=("columns")
#d=p.read_csv("aug_test.csv",skiprows=[0,3])
d=p.read_csv("aug_test.csv",nrows=100)
print (d)
g=p.read_csv("zomato.csv",sep="\t",encoding="latin_1")