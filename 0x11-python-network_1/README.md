# Python HTTP Requests and Data Manipulation

This repository contains examples and explanations on how to fetch internet resources using Python, decode response bodies, and manipulate data from external services. It covers both `urllib` and `requests` packages, showing how to make different types of HTTP requests and handle JSON resources.

## Table of Contents

1. [Fetching Internet Resources with urllib](#fetching-internet-resources-with-urllib)
2. [Decoding urllib Body Response](#decoding-urllib-body-response)
3. [Using the Python Package requests](#using-the-python-package-requests)
4. [Making HTTP GET Requests](#making-http-get-requests)
5. [Making HTTP POST/PUT/etc. Requests](#making-http-postputetc-requests)
6. [Fetching JSON Resources](#fetching-json-resources)
7. [Manipulating Data from an External Service](#manipulating-data-from-an-external-service)

## Fetching Internet Resources with urllib

To fetch internet resources using `urllib`, you can use the following example:

```python
import urllib.request as request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    html = response.read()
    print(html)

Decoding urllib Body Response

To decode the body response fetched using urllib, use the decode method:

python

import urllib.request as request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    html = response.read()
    print(html.decode('utf-8'))

Using the Python Package requests

The requests package is simpler and more powerful than urllib. It allows you to make HTTP requests easily:

python

import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print(response.text)

Making HTTP GET Requests

Using requests to make an HTTP GET request:

python

import requests

response = requests.get('https://api.example.com/resource')
print(response.json())

Making HTTP POST/PUT/etc. Requests

Using requests to make HTTP POST/PUT/DELETE requests:

python

import requests

# POST request
response = requests.post('https://api.example.com/resource', data={'key': 'value'})
print(response.json())

# PUT request
response = requests.put('https://api.example.com/resource/1', data={'key': 'new_value'})
print(response.json())

# DELETE request
response = requests.delete('https://api.example.com/resource/1')
print(response.status_code)

Fetching JSON Resources

Fetching and parsing JSON resources using requests:

python

import requests

response = requests.get('https://api.example.com/resource')
data = response.json()
print(data)

Manipulating Data from an External Service

To manipulate data from an external service, first fetch the data, then process it as needed. For example:

python

import requests

response = requests.get('https://api.example.com/resource')
data = response.json()

# Process the data
for item in data:
    print(item['name'])

## Conclusion

This guide provides a basic understanding of how to fetch and manipulate internet resources using Python. The requests package is recommended for most use cases due to its simplicity and power. Happy coding!

```javascript

This `README.md` file provides an overview of the tasks you mentioned, with examples for both `urllib` and `requests` packages.
```
