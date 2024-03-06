import requests
import json

class Conn:
    def getConn(self,api):
        response=requests.get(f"{api}")
        if(response.status_code==200):
            print("sucessfull")
            self.printdata(response.json())

        else:
            print(f"there is a {response.status_code} error")


    def printdata(self,obj):
        text=json.dumps(obj,sort_keys=True,indent=4)
        print(text)


    

    headers={"content-Type":"applicatio/json"}




    def __init__(self,api):
        self.getConn(api)


if __name__ == "__main__":
    api_call=Conn("https://fakestoreapi.com/products")