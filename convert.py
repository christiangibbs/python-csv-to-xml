# Convert .csv to .xml
# Christian J. Gibbs - 05/10/2015
# The first row of the .csv file must be headers

import csv
import datetime
now = datetime.datetime.now()

# Variables for date and time
day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)

# Take input.csv and set the file output to have a unique name
csvFile = 'raw/input.csv'
xmlFile = 'complete/13088' + day + month + year + hour + minute + second + '.xml'

# Open the csv file to read
csvData = csv.reader(open(csvFile))

# Open xml file created earlier and write a header
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
xmlData.write('<Orders>' + "\n")
xmlData.write('<Order>' + "\n")
xmlData.write('<Order_Date><![CDATA[' + day + '/' + month +'/' + year + ']]></Order_Date>' + "\n")

# Add your order ID format - example. ID-00000
xmlData.write('<Order_ID><![CDATA[DT-13088' + day + month + year + hour + minute + second + ']]></Order_ID>' + "\n")

# Add your customer ID - example. ID000
xmlData.write('<Customer_ID><![CDATA[DEPN000]]></Customer_ID>' + "\n")
xmlData.write('<Products>' + "\n")

# Parse the csv file and write the styled information to an xml file
rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
            if tags[i] == '_SKU':
                tags[i] = tags[i].replace('_SKU', 'SKU')
            else:
                tags[i] == tags[i]

            if tags[i] == '_Quantity_':
                tags[i] = tags[i].replace('_Quantity_', 'Quantity')
            else:
                tags[i] == tags[i]


    else:
        xmlData.write('<Item>' + "\n")
        for i in range(len(tags)):
            xmlData.write('<' + tags[i] + '>' \
                          + '<![CDATA[' + row[i] + ']]>' + '</' + tags[i] + '>' + "\n")
        xmlData.write('</Item>' + "\n")

    rowNum +=1

xmlData.write('</Products>' + "\n")
xmlData.write('</Order>' + "\n")
xmlData.write('</Orders>' + "\n")

xmlData.close()
