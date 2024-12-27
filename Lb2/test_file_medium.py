import requests


url = "http://127.0.0.1:8000/data"

headers_json = {'Content-Type': 'application/json'}
response_json = requests.get(url, headers=headers_json)
print("JSON Response:", response_json.text)

print('-----')

headers_xml = {'Content-Type': 'application/xml'}
response_xml = requests.get(url, headers=headers_xml)
print("XML Response:", response_xml.text)

print('-----')

response_plain = requests.get(url)
print("Plain Text Response:", response_plain.text)

print('-----')
