import requests #sends requests to websites and they return things
import json
import time
from twilio.rest import Client
while True:
    url_base = "https://www.kyliecosmetics.com/products.json?limit=250"
    url_base2 = url_base + "&page=2"
    response = requests.get(url_base) #asks for info from this website
    response2 = requests.get(url_base2)
    products = json.loads(response.content)["products"] #returns dictionary of file
    products2 = json.loads(response2.content)["products"]
    for i in [*products, *products2]:
        if(i["title"] == "So Cute | Gloss"):
            status = (i["variants"][0]['available'])
            if status == True:
                print("Available")
                client = Client("AC1ce852fac36231b042a62828199d1418", "c0fcdeebd3123e8e78f1e3c4dba45ed4")
                client.messages.create(to="+18186182912",
                                       from_="+12517664063",
                                       body="Product available")
                break
            else:
                print("Not Available")
                print(time.ctime(time.time()))
    time.sleep(3600)