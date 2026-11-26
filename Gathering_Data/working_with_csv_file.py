import pandas as p
d= p.read_csv("aug_test.csv")
g=p.read_csv("mtcars.tsv", sep="\t",names=["no","name","model","range","version","sr_code","full_code_b","1","2","3","4","5","6"])
#print (d)
print (g)