# Import necessary modules
import requests                # For making HTTP requests to fetch the webpage
from bs4 import BeautifulSoup  # For parsing HTML and XML documents
import pandas as pd            # For data manipulation and analysis
from io import StringIO        # For handling string data as file-like objects
import json
# def train_location():  
#     try:  
#         train_no = input("Enter the train number: ")
#         url = "https://www.railyatri.in/live-train-status/" + train_no 

#         # Make an HTTP GET request to fetch the webpage content
#         data = requests.get(url).text 
#         # print(data)
#         # Parse the fetched HTML content using BeautifulSoup
#         source_page = BeautifulSoup(data, 'html.parser') 
#         # print(source_page)
#         data = [] 

#         # Traverse the parsed HTML to find all 'script' tags with type "application/ld+json"
#         for item in source_page.find_all('script', type="application/ld+json"): 
#             data.append(item.get_text()) 
#         # Convert the JSON string from the third element in the data list into a StringIO object
#         json_string = StringIO(data[2]) 

#         # # Read the JSON string into a Pandas DataFrame
#         df = pd.read_json(json_string)
#         # specific information from the DataFrame
#         # print(df)
#         print(df["mainEntity"][0]['acceptedAnswer']['text']) 
#     except KeyError:
#         print(f"{train_no} complete our destination")

def station_train_stop():
#     # no of trains stops in the railway station
    url= "https://indianrailapi.com/api/v2/AllTrainOnStation/apikey/e4d438952802b5eb15b4003e767baded/StationCode/DMO/"
    data = requests.get(url).text
    A=json.loads(data)
    # print(A)
    print(1,">>",A["Trains"][0])
    for i in range(0,len(A["Trains"])):
        print(i+1,">>",A["Trains"][i])
        print("------------------------------------------------------------------------------------------------------------")
station_train_stop()
# train_location()
# import requests
# import json
# url= "https://indianrailapi.com/api/v2/TrainNumberToName/apikey/e4d438952802b5eb15b4003e767baded/TrainNumber/20971/"
# # url =""
# data = requests.get(url).text
# A=json.loads(data)
# print(A)



# route of train
url= "http://indianrailapi.com/api/v2/TrainSchedule/apikey/e4d438952802b5eb15b4003e767baded/TrainNumber/20971/"
# url =""
data = requests.get(url).text
A=json.loads(data)
print(A)
for i in range(0,len(A["Route"])):
    print(i+1,">>",A["Route"][i])
    print("------------------------------------------------------------------------------------------------------------")
print(A)





