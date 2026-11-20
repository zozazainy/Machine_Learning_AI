import mysql.connector
import pandas as p
from sqlalchemy import create_engine, URL

# d = p.read_json('hotels_zoza.json')
# print(d)





engine = create_engine(
    URL.create(
        drivername="mysql+pymysql",
        username="root",
        password="",
        host="localhost",
        database="world"
    )
)

df = p.read_sql_query("SELECT * FROM countrylanguage", engine)

print(df)