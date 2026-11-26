import pandas as p
from data_profiling import ProfileReport as r

d = p.read_csv("tips.csv")
prof = r(d)
prof.to_file(output_file="output.html")
