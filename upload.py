from elasticsearch import Elasticsearch, helpers
import csv
import time
es = Elasticsearch(hosts="192.168.1.114")
j = 0
actions = []
with open('/Users/willian/Desktop/go_es.csv',newline='') as csvFile:
    spamreader = csv.reader(csvFile)
    for row in spamreader:
        # print(row)
        # print(', '.join(row))
        if row[0] == 'id':
            continue
        strptime = time.strptime(row[11], "%Y-%m-%d")
        time_stamp = int(time.mktime(strptime))
        action = {
            "_index": "tickets-index",
            "_type": "tickets",
            "_id": j,
            "_source": {
                "OrderId": row[0],
                "MudiPort": row[13],
                "Purchaser": row[5],
                "PurchaserAddress": row[6],
                "SupplierId": row[7],
                "PurchaserId": row[4],
                "OrderNo": row[1],
                "OrderWeight": row[2],
                "Supplier": row[8],
                "ProDesc": row[10],
                "OriginalCountry": row[14],
                "SupplierAddress": row[9],
                "FrankTime": time_stamp,
                "OrderVolume": row[3],
                "QiyunPort": row[12],
                "TradeNumber": 0
            }
        }
        actions.append(action)
        j += 1
        if j >= 1000:
            helpers.bulk(es, actions)
            actions.clear()





