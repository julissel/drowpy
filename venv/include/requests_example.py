import requests
import json
import re


# Make a simple request
r = requests.get('http://httpbin.org/get')
print(r.text)

r1 = requests.post('http://httpbin.org/post')
print(r.text)

# Passing some parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r3 = requests.get('http://httpbin.org/get', params=payload)
print(r3.text)

r4 =requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r4.text)


# passing json
url = 'http://httpbin.org/post'
# 1 way - serialize json
rj = requests.post(url, data=json.dumps({'key':'value'}))
# 2 way - use built-in mechanism
rj = requests.post(url, json={'key':'value'})
print(rj.text)

# post a multipart-encoded file
url = 'http://httpbin.org/post'
files = {'file':
         ('test.txt',
          open('/home/julia/Books/coursera_python_WEB/test_text.txt',
               'rb'))}

rf = requests.post(url, files=files)
print(rf.text)


# headers
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

rh = requests.get(url, headers=headers)
print(r.text)


# response content
r = requests.get('http://httpbin.org/get')
print(type(r.text), r.text)
print(type(r.content), r.content)
print(type(r.json), r.content)


# response status codes
print(r.status_code)
print(requests.codes.ok)


# response headers
print(r.headers)


# redirection and history
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

r = requests.get('http://github.com', allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history)


# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)


# session objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)


# re
result = requests.get("http://cbr.ru")
html = result.text
match = re.search(r"Евро\D+(\d+,\d+)", html)
rate = match.group(1)
print("The Euro rate = ", rate)


print("")
bad_req = requests.get('http://httpbin.org/status/404')
print(bad_req.status_code)
bad_req.raise_for_status()