from bs4 import BeautifulSoup
import re
import requests


html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>test page</title>
  </head>
  <body class="mybody" id="js-body">
    <p class="text odd">first <b>bold</b> paragraph</p>
    <p class="text even">second <a href="https://mail.ru">link</a></p>
    <p class="list odd">third <a id="paragraph"><b>bold link</b></a></p>
  </body>
</html>
"""


soup = BeautifulSoup(html, 'lxml')

print(soup.prettify())
print()
print(f"Value of <p> <b> = '{soup.p.b.string}'")
print()
print("List of names in class <p>")
print(soup.p['class'])
print()
print(f"Value of <body> id = '{soup.body['id']}'")
print()
print("Parent tag of 'b':")
print(soup.p.b.parent)
print()
print("All parents of tag 'b':")
print([tag.name for tag in soup.p.b.parents])
print()
print(f"Next element for tag <p> = '{soup.p.next.next}'")
print()
print("Next tag with class 'even' for tag <p> = ", soup.p.find_next_sibling(class_="even"))
print()
print("all tags <p>:")
print(soup.find_all('p'))
print()
print("find class_ 'odd' and class_ 'text' in the strict order (1-st version):",
      soup.find_all(name='p', class_='text odd'))
print()
print("find class_ 'odd' and class_ 'text' in the strict order (2-st version):",
      soup.find_all('p', 'text odd'))
print()
print("find class_ 'odd' and class_ 'text' in the strict order (no results):",
      soup.find_all('p', 'odd text'))
print()
print("find class_ 'odd' and class_ 'text' without any order (using css-selector):",
      soup.select('p.odd.text'))
print()
print("find tag <b> included into tag <a> (using css-selector):",
      soup.select("a > b"))
print()
print("find all tags wich starting from 'b' (using re):")
print([i.name for i in soup.find_all(name=re.compile('^b'))])


result = requests.get("https://news.mail.ru/")
html_new = result.text
soup_new = BeautifulSoup(html_new, 'lxml')

news = [(section.string,
        [link.string for link in section.find_parents()[4].find_all('span', 'link__text')])
       for section in soup_new.find_all('span', 'hdr__inner')]
for val in news:
    print(val)

