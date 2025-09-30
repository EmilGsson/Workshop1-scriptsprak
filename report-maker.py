# Import the json library so that we can handle json
import json



# Read json from products.json to the variable products
data = json.load(open("network_devices.json", "r", encoding = "utf-8"))

# create a variable that holds our whole text report

report = ""

## print company name and last_updated from json
report += data["company"] + " | " + data["last_updated"] + "\n\n"

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

        

##write the report to text file

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
    