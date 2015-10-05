# Convert .csv to .xml
# Christian J. Gibbs - 05/10/2015
# The first row of the .csv file must be headers

import csv
import datetime
now = datetime.datetime.now()


day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)

csvFile = 'input.csv'
xmlFile = 'output' + day + month + year + hour + minute + second + microsecond + '.xml'


csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"? encoding="ISO-8859-1" ?>' + "\n")
xmlData.write('<Orders>' + "\n")
xmlData.write('<Order>' + "\n")
xmlData.write('<Order_Date><![CDATA[ENTER ORDER DATE (DD/MM/YYYY)]]></Order_Date>' + "\n")
xmlData.write('<Order_ID><![CDATA[ENTER ORDER ID]]></Order_ID>' + "\n")
xmlData.write('<Customer_ID><![CDATA[ENTER CUSTOMER ID]]></Customer_ID>' + "\n")
xmlData.write('<Products>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<Item>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + '<![CDATA[' + row[i] + ']]>' + '</' + tags[i] + '>' + "\n")
        xmlData.write('</Item>' + "\n")

    rowNum +=1

xmlData.write('<Products>' + "\n")
xmlData.write('<Order>' + "\n")
xmlData.write('</Orders>' + "\n")

xmlData.close()
