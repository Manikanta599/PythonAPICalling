import requests
import json

import requests
import json

def adding():
    url = "https://fakestoreapi.com/products"

    data = {
        "title": "Shirt",
        "price": 1500,
        "description": "Trends Brand",
    }
   
    headers = {"Content-Type": "application/json"}  

    response = requests.post(url, json=data, headers=headers)

    print(response.json())

adding()



