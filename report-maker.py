# Import the json library so that we can handle json
import json



# Read json from products.json to the variable products
data = json.load(open("network_devices.json", "r", encoding = "utf-8"))


#loop location list
#location lista av "locations" i json-fil

for location in data["locations"]:
    #print the site
    print (location ["site"])
    #print hostname devicers on locations
    for device in location ["devices"]:
        print(" ", device["hostname"])