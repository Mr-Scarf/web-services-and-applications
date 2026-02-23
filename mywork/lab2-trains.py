import requests
import csv
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# print(doc.toprettyxml())  # commented out

retrieveTags = [
    'TrainStatus',
    'TrainLatitude',
    'TrainLongitude',
    'TrainCode',
    'TrainDate',
    'PublicMessage',
    'Direction'
]

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(
        train_file, 
        delimiter='\t', 
        quotechar='"', 
        quoting=csv.QUOTE_MINIMAL
    )
    
    train_writer.writerow(retrieveTags)  # write header

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()

        # Only store trains whose code starts with "D"
        if traincode.startswith('D'):
            dataList = []
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                value = datanode.firstChild.nodeValue.strip() if datanode.firstChild else ''
                dataList.append(value)

            print(dataList)  # prints one complete row per train
            train_writer.writerow(dataList)