import sys
import requests

url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Timeout error, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print(f"Error url: {url}, code {code}")
except requests.RequestException:
    print("Downloading error url:", url)
else:
    print(response.content)
