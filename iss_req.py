import requests
import sys
url = "http://api.open-notify.org/"
def getLatLong():
    request = requests.get(url+"iss-now.json")
    data = request.json()["iss_position"]
    print ("----- ISS LAT LONG -----")
    print "Lat ", data["latitude"]
    print "Long ", data["longitude"]
def getAstronaut():
    request = requests.get(url+"astros.json")
    data = request.json()["people"]
    print ("----- ISS ASTRONAUT -----")
    for i in data:
        print "Name ", i["name"]

arg = str(sys.argv[1])

if arg == "location":
    getLatLong()
else:
    getAstronaut()