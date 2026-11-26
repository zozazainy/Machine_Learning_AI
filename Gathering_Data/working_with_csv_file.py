
import pandas as p

# 1. Reading a TSV file and assigning column names
g = p.read_csv(
    "mtcars.tsv",
    sep="\t",
    names=["no", "name", "model", "range", "version",
           "sr_code", "full_code_b", "1", "2", "3", "4", "5", "6"]
)
print(g)


# 2. Reading CSV with header=1
d = p.read_csv("aug_test.csv", header=1)
print(d)


# 3. Reading selected columns
d = p.read_csv("aug_test.csv", usecols=["enrollee_id", "city"])
print(d)


# 4. Converting a single-column DataFrame into a Series
d = p.read_csv("aug_test.csv", usecols=["enrollee_id"]).squeeze("columns")
print(d)


# 5. Skipping specific rows
d = p.read_csv("aug_test.csv", skiprows=[0, 3])
print(d)


# 6. Reading only the first 100 rows
d = p.read_csv("aug_test.csv", nrows=100)
print(d)


# 7. Reading Zomato dataset
g = p.read_csv("zomato.csv", sep="\t", encoding="latin-1")
print(g)


# 8. Reading Books dataset
h = p.read_csv(
    "BX-Books.csv",
    sep=";",
    encoding="latin-1",
    escapechar="\\"
)
print(h)


# 9. Converting decimal column into integer
l = p.read_csv("aug_test.csv")

# Multiply by 1000 to preserve decimal information
l["city_development_index"] = (
    l["city_development_index"] * 1000
).round().astype("Int64")

print(l["city_development_index"])
print(l.info())


# 10. Parsing dates
o = p.read_csv(
    "IPL Matches 2008-2020.csv",
    parse_dates=["date"]
)
print(o)


# 11. Using converters to replace umpire names
def rename(name):
    if name == "Asad Rauf":
        return "zozazainy"
    else:
        return name


o = p.read_csv(
    "IPL Matches 2008-2020.csv",
    converters={
        "umpire1": rename,
        "umpire2": rename
    }
)

print(o[["umpire1", "umpire2"]])
