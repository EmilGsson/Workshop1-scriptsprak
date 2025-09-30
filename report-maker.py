# Import the json library so that we can handle json
import json



# Read json from products.json to the variable products
data = json.load(open("network_devices.json", "r", encoding = "utf-8"))

# create a variable that holds our whole text report

report = ""

#count variabel for counting types

count = 0

## print company name and last_updated from json
report += data["company"] + " | " + data["last_updated"] + "\n\n"

#variabele for counting units
count = {}

#loop location list
#location lista av "locations" i json-fil
for location in data["locations"]:
    #print the site
    report += location ["site"] +"\n"
   
        #print hostname devicers on locations
    for device in location ["devices"]:
        report += "  " + device["hostname"] + "\n"
        # IF status != (is not) online, print status
        if device["status"] != "online":
            report +=  device["hostname"] + " | " + device ["status"] + "\n"
            

#variabele for counting units.Tried = 0 and it does not allow to find (what i cound find)
count = {}

##loop list to find all variables in type and count them with "get" https://www.w3schools.com/python/ref_dictionary_get.asp

for location in data["locations"]:
    for device in location["devices"]:
        x = device.get("type")
        ## this code under printed all types in the terminal showing my loop worked. just for fun
        ###print (x) 
        count [x] = count.get(x, 0) +1

#writes this text to make document look better       
report += "Type of devices:\n"
        
## for "x" in count (variable i created) write x + count in the text file. 
for x in count:                       
    report += x +  ": " + str(count[x]) + "\n"
            
#for text format            
report += "\nDevices with less than 30 days uptime:\n"

for location in data["locations"]:
    for device in location["devices"]:
        if device["uptime_days"] < 30:
            report += device["hostname"] + " | " + str(device["uptime_days"]) + " days\n"
        
        
##write the report to text file

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
    