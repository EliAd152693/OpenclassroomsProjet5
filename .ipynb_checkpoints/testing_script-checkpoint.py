import json, requests

data = 'python code for testing'

j_data=json.dumps(data)
headers= {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post('http://127.0.0.1:5000/api/', data=j_data, headers=headers)
print(r.text)
