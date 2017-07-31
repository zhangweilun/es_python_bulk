from elasticsearch import Elasticsearch,helpers
es = Elasticsearch(hosts="192.168.1.114")
j = 0
actions = []
while j <= 100000:
    action = {
        "_index": "tickets-index",
        "_type": "tickets",
        "_id": j,
        "_source": {
            "any":"data" + str(j),
            "timestamp": datetime.now()
            }
        }
    actions.append(action)
    j += 1

helpers.bulk(es, actions)
