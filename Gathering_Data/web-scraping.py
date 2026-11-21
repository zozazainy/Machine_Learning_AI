
import pandas as p
import requests
from bs4 import BeautifulSoup as b

url = 'https://books.toscrape.com/'

y = requests.get(url)
soup = b(y.text, 'lxml')

# Main scraping code
d = soup.find_all('article', class_='product_pod')

mylist = []

for i in d:

    title = i.h3.a['title']
    price = i.find('p', class_='price_color').text
    availability = i.find(
        'p', class_='instock availability'
    ).get_text(strip=True)

    mylist.append({
        'Title': title,
        'Price': price,
        'Availability': availability
    })

df = p.DataFrame(mylist)

df.to_csv('Books-to-scrape.csv', index=False, encoding='utf-8-sig')

print(df)
print('CSV file created successfully!')


# Your BeautifulSoup experiments
print(soup.prettify())

print(soup.find('h1'))
print(soup.find('h1').text.strip())

print(len(soup.find_all('p', class_='star-rating Three')))

company = soup.find_all('article', class_='product_pod')

print(company)
print(len(company))


# Finding breadcrumb
print(soup.find('p', class_='breadcrumb'))

# Finding all paragraphs
print(soup.find_all('p'))

# Finding h1
print(soup.find('h1'))
