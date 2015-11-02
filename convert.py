# Convert .csv to .xml
# Christian J. Gibbs - 05/10/2015
# The first row of the .csv file must be headers

import os, os.path
import glob
import shutil
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

# Check for files in /raw folder
files = glob.glob("raw/*.csv")
file_count = len(files)
dir = "raw/"

for i in range(len(files)):

    # Take input.csv and set the file output to have a unique name
    csvFile = files[i]
    xmlFile = 'complete/13088' + day + month + year + hour + minute + second + str(i) + '.xml'

    # Remove directorry
    file = csvFile.strip(dir)

    # Open the csv file to read
    csvData = csv.reader(open(csvFile))

    # Open xml file created earlier and write a header
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
    xmlData.write('<Orders>' + "\n")
    xmlData.write('<Order>' + "\n")
    xmlData.write('<Order_Date><![CDATA[' + day + '/' + month +'/' + year + ']]></Order_Date>' + "\n")

    # Add your order ID format - example. ID-00000
    xmlData.write('<Order_ID><![CDATA[DT-13088' + day + month + year + hour + minute + second + str(i) + ']]></Order_ID>' + "\n")

    # Add your customer ID - example. ID000
    xmlData.write('<Customer_ID><![CDATA[DEPN000]]></Customer_ID>' + "\n")
    xmlData.write('<Products>' + "\n")

    # Parse the csv file and write the styled information to an xml file
    rowNum = 0
    #rowCount = sum(1 for row in csvData)
    #rowFault = rowCount - 1
    #print rowFault

    for row in csvData:

        if rowNum == 0:
            tags = row
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
                # Fix SKU
                if tags[i] == '_SKU':
                    tags[i] = tags[i].replace('_SKU', 'SKU')
                else:
                    tags[i] == tags[i]
                # Fix Quantity
                if tags[i] == '_Quantity':
                    tags[i] = tags[i].replace('_Quantity', 'Quantity')
                else:
                    tags[i] == tags[i]

                # Fix Item Description
                if tags[i] == '_Item_Description':
                    tags[i] = tags[i].replace('_Item_Description', 'Item_Description')
                else:
                    tags[i] == tags[i]

                # Fix Product Variation Details
                if tags[i] == '_Product_Variation_Details':
                    tags[i] = tags[i].replace('_Product_Variation_Details', 'Product_Variation_Details')
                else:
                    tags[i] == tags[i]


        else:
            xmlData.write('<Item>' + "\n")
            for i in range(len(tags)):
                # Remove unwanted export data
                if row[i] == "null":
                    row[i] = row[i].replace('null', '')

                # Write to xml file
                xmlData.write('<' + tags[i] + '>' \
                                  + '<![CDATA[' + row[i] + ']]>' + '</' + tags[i] + '>' + "\n")

            xmlData.write('</Item>' + "\n")

        rowNum +=1

    xmlData.write('</Products>' + "\n")
    xmlData.write('</Order>' + "\n")
    xmlData.write('</Orders>' + "\n")

    xmlData.close()

#print('Complete: ' + file)
# print('Progress: ' + str(progress) + '%')

    # Move file to other folder when processing automatically - avoids duplicate processing
    # Does not work with Windows, tested and working on Linux and MacOS
    # shutil.move("raw/" + file, "processed/" + file)
# print('Progress: 100%')
