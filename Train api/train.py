# Import necessary modules
import requests                # For making HTTP requests to fetch the webpage
# from bs4 import BeautifulSoup  # For parsing HTML and XML documents
import pandas as pd            # For data manipulation and analysis
from io import StringIO        # For handling string data as file-like objects
import json
import time
featurs=["live location"]
# train live status:
train_no= input("Enter the train number :- ")
date=time.strftime("%Y%m12")
apikey="e4d438952802b5eb15b4003e767baded"
trainNumber="22162"
stationFrom='DMO'
stationTo='BPL'
yyyyMMdd="20240814"
classCode="SL"
url = f"https://indianrailapi.com/api/v2/SeatAvailability/apikey/{apikey}/TrainNumber/{trainNumber}/From/{stationFrom}/To/{stationTo}/Date/{yyyyMMdd}/Quota/GN/Class/{classCode}"
ht= requests.get(url).text
data= json.loads(ht)
print(data)

# url= "https://indianrailapi.com/api/v2/TrainNumberToName/apikey/e4d438952802b5eb15b4003e767baded/TrainNumber/12176/"
# # url =""
# data = requests.get(url).text
# A=json.loads(data)
# print(A)