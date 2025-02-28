# info={"status":True,"message":"Success","timestamp":1723732349875,
#     "data":{"Pnr":"2646353153","TrainNo":"12176","TrainName":"CHAMBAL EXPRESS","Doj":"07-09-2024","BookingDate":"14-07-2024","Quota":"PQ","DestinationDoj":"08-09-2024","SourceDoj":"07-09-2024","From":"MRPR","FromStnActual":"null","To":"PNME","ReservationUpto":"PNME","BoardingPoint":"MRPR","Class":"SL","ChartPrepared":False,"BoardingStationName":"Mau Ranipur","TrainStatus":"","TrainCancelledFlag":False,"ReservationUptoName":"Parasnath","PassengerCount":4,
#             "PassengerStatus":[{"ReferenceId":"null","Pnr":"null","Number":1,"Prediction":"Available","PredictionPercentage":"null","ConfirmTktStatus":"Confirm","Coach":"S3","Berth":34,"BookingStatus":"CNF S3 34","CurrentStatus":"CNF","CoachPosition":"null","BookingBerthNo":"34","BookingCoachId":"S3","BookingStatusNew":"CNF","BookingStatusIndex":"0","CurrentBerthNo":"","CurrentCoachId":"","BookingBerthCode":"MB","CurrentBerthCode":"null","CurrentStatusNew":"CNF","CurrentStatusIndex":"0"},
#                                {"ReferenceId":"null","Pnr":"null","Number":2,"Prediction":"Available","PredictionPercentage":"null","ConfirmTktStatus":"Confirm","Coach":"S3","Berth":35,"BookingStatus":"CNF S3 35","CurrentStatus":"CNF","CoachPosition":"null","BookingBerthNo":"35","BookingCoachId":"S3","BookingStatusNew":"CNF","BookingStatusIndex":"0","CurrentBerthNo":"","CurrentCoachId":"","BookingBerthCode":"UB","CurrentBerthCode":"null","CurrentStatusNew":"CNF","CurrentStatusIndex":"0"},
#                                {"ReferenceId":"null","Pnr":"null","Number":3,"Prediction":"Available","PredictionPercentage":"null","ConfirmTktStatus":"Confirm","Coach":"S3","Berth":37,"BookingStatus":"CNF S3 37","CurrentStatus":"CNF","CoachPosition":"null","BookingBerthNo":"37","BookingCoachId":"S3","BookingStatusNew":"CNF","BookingStatusIndex":"0","CurrentBerthNo":"","CurrentCoachId":"","BookingBerthCode":"MB","CurrentBerthCode":"null","CurrentStatusNew":"CNF","CurrentStatusIndex":"0"},
#                                {"ReferenceId":"null","Pnr":"null","Number":4,"Prediction":"Available","PredictionPercentage":"null","ConfirmTktStatus":"Confirm","Coach":"S3","Berth":38,"BookingStatus":"CNF S3 38","CurrentStatus":"CNF","CoachPosition":"null","BookingBerthNo":"38","BookingCoachId":"S3","BookingStatusNew":"CNF","BookingStatusIndex":"0","CurrentBerthNo":"","CurrentCoachId":"","BookingBerthCode":"UB","CurrentBerthCode":"null","CurrentStatusNew":"CNF","CurrentStatusIndex":"0"}],
#             "DepartureTime":"10:18","ArrivalTime":"01:19","ExpectedPlatformNo":"1","BookingFare":"1820","TicketFare":"1820","CoachPosition":"L SLR GEN GEN GEN GEN S8 S7 S6 S5 S4 S3 S2 S1 B4 B3 B2 B1 A2 A1 SLR","Rating":3.5,"FoodRating":3.2,"PunctualityRating":3.5,"CleanlinessRating":3.8,"SourceName":"Mau Ranipur","DestinationName":"Isri","Duration":"15:1","RatingCount":570,"HasPantry":False,"GroupingId":"null","OptVikalp":False,"VikalpData":"","VikalpTransferred":False,"VikalpTransferredMessage":"",
#             "FromDetails":{"category":"D","division":"JHS","latitude":"27.1578152","longitude":"77.9899244","state":"UTTAR PRADESH","stationCode":"MRPR","stationName":"MAURANIPUR"},
#             "ToDetails":{"category":"A","division":"DHN","latitude":"23.987568","longitude":"86.0373974","state":"JHARKHAND","stationCode":"PNME","stationName":"PARASHNATH"},
#             "BoardingPointDetails":{"category":"D","division":"JHS","latitude":"27.1578152","longitude":"77.9899244","state":"UTTAR PRADESH","stationCode":"MRPR","stationName":"MAURANIPUR"},
#             "ReservationUptoDetails":{"category":"A","division":"DHN","latitude":"23.987568","longitude":"86.0373974","state":"JHARKHAND","stationCode":"PNME","stationName":"PARASHNATH"}}}
# # import requests

# # url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"

# # querystring = {"pnrNumber":"2700709289"}

# # headers = {
# # 	"x-rapidapi-key": "ff3a943637msh0da6e83acca135dp105fc8jsndec2ee9b661d",
# # 	"x-rapidapi-host": "irctc1.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)
# # info=response.json()
# # # print(response.json())
# print(info["data"]["Doj"],"                     ",info["data"]["DestinationDoj"])
# print(" ",info["data"]["DepartureTime"],"----------",info["data"]["Duration"],"----------",info["data"]["ArrivalTime"])
# print(" ",info["data"]["From"],"                           ",info["data"]["To"])
# print(info["data"]["FromDetails"]["stationName"],"                     ",info["data"]["ToDetails"]["stationName"])
# print("PNR  : ",info["data"]["Pnr"])
# print("Class: ",info["data"]["Class"])
# print("Class: ",info["data"]["ChartPrepared"])
# for i in range(len(info["data"]["PassengerStatus"])):
#     print("Passenger :",info["data"]["PassengerStatus"][i]["Number"])
#     print(info["data"]["PassengerStatus"][i]["BookingCoachId"],"-",info["data"]["PassengerStatus"][i]["BookingBerthCode"],"-",
#           info["data"]["PassengerStatus"][i]["BookingBerthNo"],"::",info["data"]["PassengerStatus"][i]["CurrentStatusNew"])


# import yt_dlp

# ydl_opts = {}

# def dwl_vid(video_url):
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

# channel = 1
# while channel == 1:
#     link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download: ")
#     zxt = link_of_the_video.strip()

#     dwl_vid(zxt)
#     channel = int(input("Enter 1 if you want to download more videos\nEnter 0 if you are done: "))

