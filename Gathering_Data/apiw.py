import pandas as p
import requests

url = 'https://api.github.com/gists/406b843afdfb9c6a86e25753fe2761f4'

response = requests.get(url)

data = response.json()

raw_url = data['files']['Film.JSON']['raw_url']

film_response = requests.get(raw_url)

films = film_response.json()

df = p.DataFrame(films)

print(df[['Title', 'Year']])
df.to_csv('actioned_movies.scv')
