import requests
import re
from bs4 import BeautifulSoup


resp = requests.get("https://wikipedia.org/")
html = resp.text

# 1
# with re
res = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
print(res)

# 2
# with BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print([tag['href'] for tag in soup('a', 'other-project-link')])

