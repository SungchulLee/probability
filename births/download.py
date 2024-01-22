import requests
import os

def download():
    url = "https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv"
    local_filename = "./data/births.csv"
    if not os.path.exists(local_filename):
        os.makedirs("./data",exist_ok=True)

        response = requests.get(url)
        with open(local_filename, 'wb') as file:
            file.write(response.content)