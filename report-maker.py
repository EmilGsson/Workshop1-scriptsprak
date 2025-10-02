# Import the json library so that we can handle json
import json



# Read json from products.json to the variable products
data = json.load(open("network_devices.json", "r", encoding = "utf-8"))

# create a variable that holds our whole text report

report = ""

## print company name and last_updated from json
## use () to format text better

report += (
"=========================================================================================\n" + "\n" +
 data["company"] + " | " + data["last_updated"] + "\n\n" + 
"=========================================================================================\n" + "\n")



  
report += "Overview" + "\n-----------------------------------------------------------------------------------------\n"
##print total % usage of switch ports
total_used = 0
total_ports = 0

for location in data["locations"]:
    for device in location["devices"]:
        if device.get("type") == "switch":
            ports = device.get("ports")
            if ports:
                total_used += ports["used"]
                total_ports += ports["total"]

percent = round(total_used / total_ports * 100, 1)

report += ("Total switch port usage: "
            + str(total_used) + "/"
            + str(total_ports) + " (" 
            + str(percent) + "%)\n" + "\n")

  
#print hostname devicers on locations
report += "Warnings: \n"
for location in data["locations"]:
    for device in location ["devices"]:
       # report += "  " + device["hostname"] + "\n"
        # IF status != (is not) online, print status
        if device["status"] != "online" and device["status"] != "offline" :

            report += (
                    device["hostname"].ljust(20) + " |- "
                     + device["status"].ljust(10) + " | "
                     + device["type"].ljust(15) + " | "
                     + location["site"].ljust(20)
                     + "\n")


##same loop but print offline not warning
report += "\n" + "Offline: \n"
for location in data["locations"]:
    for device in location ["devices"]:
       # report += "  " + device["hostname"] + "\n"
        # IF status != (is not) online, print status
        if device["status"] != "online" and device["status"] != "warning":
           report += (
                 device["hostname"].ljust(20) + " |- "
                + device["status"].ljust(10) + " | "
                + device["type"].ljust(15) + " | "
                + location["site"].ljust(20)
                + "\n"
)



report += "-----------------------------------------------------------------------------------------\n" + "\n"



count = {} #variabele for counting units.Tried = 0 and it does not allow to find (what i cound find)
##loop list to find all variables in type and count them with "get" https://www.w3schools.com/python/ref_dictionary_get.asp
for location in data["locations"]:
    for device in location["devices"]:
        x = device.get("type")
        ## this code under printed all types in the terminal showing my loop worked. just for fun
        ###print (x) 
        count [x] = count.get(x, 0) +1

#writes this text to make document look better       
report += ("Type of devices in network:\n" + 
"-----------------------------------------------------------------------------------------\n")

## for "x" in count (variable i created) write x + count in the text file. 
for x in count:                       
    report += x +  ": " + str(count[x]) + "\n" 


report +=("-----------------------------------------------------------------------------------------" + "\n\n" +
"Devices with less than 30 days uptime:\n" + 
"-----------------------------------------------------------------------------------------\n")
## all devices under 30 days uptime will be highlighted
for location in data["locations"]:
    for device in location["devices"]:
        if device["uptime_days"] < 30:
            report += device["hostname"] + " | " + str(device["uptime_days"]) + " days\n"

report += "-----------------------------------------------------------------------------------------\n" + "\n" 




port = {} ##create variable like in prev examples

report += ("Total ports of all devices" + "\n" + 
           "-----------------------------------------------------------------------------------------\n")
#used_ports = 0
#total_ports = 0

for location in data["locations"]:
    for device in location["devices"]:
        ports = device.get("ports")
        if ports: #kollar om port finns

            ##print all variables (could not find way of printing all at same time. mby revisit)
            percent = round(ports["used"] / ports["total"] * 100, 1)
            report += device["hostname"] + "  |  " 
            report += "total:" + str(ports["total"]) + ", "
            report += "used: " + str(ports["used"]) + ", "
            report += "free: " + str(ports["free"]) +"," 
            report += "usage: " + str(percent) + "% \n"

            
report += "-----------------------------------------------------------------------------------------\n"       


##write the report to text file
report += ("\nVlans used by diffrent devices" + "\n" + 
"-----------------------------------------------------------------------------------------\n")

## format for dokument
for location in data["locations"]:
    for device in location["devices"]:
        vlan  = device.get("vlans")
        if vlan: #check if vlan exist
           report += device["hostname"] + "  |  " + str(vlan) + "\n" # print hostname and str(vlan) that uses device get to get list
            
unique_vlans = set()

for location in data["locations"]:
    for device in location["devices"]:
        for v in device.get("vlans", []):
            unique_vlans.add(v)

##report += "-----------------------------------------------------------------------------------------\n"
report += "\n"+"Unique VLANs in the network (" + str(len(unique_vlans)) + "):\n"
report += ", ".join(str(v) for v in sorted(unique_vlans)) + "\n"

report += ("-----------------------------------------------------------------------------------------\n\n" +
"Total devices in region\n" + "-----------------------------------------------------------------------------------------\n")

for location in data["locations"]:
    ## counters for each location. start at 0 and if loop correct, add one
    total = 0
    online = 0
    offline = 0   # count everything not online" 

    for device in location["devices"]:## loop through all devices in this location
        total += 1
        if device.get("status") == "online":
            online += 1
        else:
            offline += 1

    ## location["site"] = the site name
    ## total = number of devices at this site
    ## online = how many are online
    ## offline = how many are not online
    
    report += location["site"] + " | total: " + str(total) + " | online: " + str(online) + " | offline: " + str(offline) + "\n"






with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
    






###########################################################################################################
#list of location, not needed. delete if bloat
#loop location list
#location lista av "locations" i json-fil
##for location in data["locations"]:
    #print the site
   ## report += location ["site"] +"\n"
###########################################################################################################  