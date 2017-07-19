import csv
from subprocess import Popen

#create csvfile to write to with designated location and file name here
csvfile = "output1.csv"

#txt file to open from nmap quick scan
f = open("file1.txt", "r")
lineitem = []
ip = ""
mac = ""
vendor = ""
i=0
items=[['IP Address','MAC Address','Vendor/Manufacturer']]
for line in f:
    ip = ""
    mac = ""
    vendor = ""
    lineitem = (line.split())
    if len(lineitem) > 0:
        if lineitem[0] == "Nmap":
            output = []
            ip = lineitem[4]
            output.append(ip)
            i+=1
        if lineitem[0] == "MAC":
            if len(lineitem) == 4:
                mac = lineitem[2]
                vendor = lineitem[-1]
                output.append(mac)
                output.append(vendor)
                items.append(output)
            elif len(lineitem) == 5:
                mac = lineitem[2]
                vendor = lineitem[-2] +" "+ lineitem[-1]
                output.append(mac)
                output.append(vendor)   
                items.append(output)
            elif len(lineitem) == 6:
                mac = lineitem[2]
                vendor = lineitem[-3] +" "+ lineitem[-2] +" "+ lineitem[-1]
                output.append(mac)
                output.append(vendor)   
                items.append(output)
            elif len(lineitem) == 6:
                mac = lineitem[2]
                vendor = lineitem[-4] +" "+ lineitem[-3] +" "+ lineitem[-2] +" "+ lineitem[-1]
                output.append(mac)
                output.append(vendor)   
                items.append(output)
                
f.close()

#open csvfile and write contents of list
with open(csvfile, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(items)

#pop open excel with newly created csvfile
p = Popen(csvfile, shell=True)
