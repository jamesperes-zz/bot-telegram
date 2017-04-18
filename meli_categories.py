
import requests
import os
import time


url="https://api.mercadolibre.com"

def getting_macro_categories(url, country):
    with open(os.path.expanduser("~/meli_categories.csv"), "w") as file_csv:
        r = requests.get(url + "/sites/{}/categories".format(country))
        r = r.json()
        for category in r:
            file_csv.write(category.get("id") + "|")
            file_csv.write(category.get("name"))
            file_csv.write("\n")

while True:
    time.sleep(10)
getting_macro_categories("https://api.mercadolibre.com", "MLB")