import requests
import json

status = "available"

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


response = requests.post(f"https://petstore.swagger.io/v2/pet",
                         headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(info, ensure_ascii=False))

print(response.status_code)
print(response.text)
print(response.json())
print(type(response.json()))

new_info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Dobbi",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
resput = requests.put(f"https://petstore.swagger.io/v2/pet", data=json.dumps(new_info, ensure_ascii=False))

print(resput.status_code)
print(resput.text)
print(resput.json())
print(type(resput.json()))

res = requests.delete(f"https://petstore.swagger.io/v2/pet/{new_info}",data=json.dumps(new_info, ensure_ascii=False))




