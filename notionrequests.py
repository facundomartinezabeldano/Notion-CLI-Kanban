import pprint
from bleach import clean
import requests
import json


pp = pprint.PrettyPrinter(indent=4)
url = "https://api.notion.com/v1/databases/63cd54d3b2254b02b9f258c52e38400a/query"
payload = {
    "page_size": 100
}

headers = {
    "Accept": "application/json",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
    "Authorization": "Bearer secret_eb1BDBMm4ZTVPqgWCJKnNapjjdPCJLQogDz4svIV1lI"
}

response = requests.request("POST", url, json=payload, headers=headers).json()


#pp.pprint(response)



'''
Quiero tener un objeto que tenga por un lado una lista de payloads y por el otro una lista de urls
    obj = {
        'payloads': [], #payloads list
        'ids': [] #string list
    }
'''

clean_payload = {
    'payloads': [], #payload list
    'ids': [], #id list
}


for page in response['results']:
    children = {
        'Task': page['properties']['Task']['title'][0]['text']['content'],
        'Status': page['properties']['Status']['multi_select'][0]['name'],
        'Short Description': page['properties']['Short Description']['rich_text'][0]['plain_text'],
        'Due date': page['properties']['Due date']['rich_text'][0]['plain_text']
    }
    clean_payload['ids'].append(page['id'])
    clean_payload['payloads'].append(children)

pp.pprint(clean_payload)
























'''
pp.pprint([ r['properties'] for r in response['results'] ])


for page in response:
    output =  {
        'Task': page['Task']['title'][0]['text']['content'],
        'Status': page['Status']['multi_select'][0]['name'],
        'Short Description': page['Short Description']['rich_text'][0]['plain_text'],
        'Due date': page['Due date']['rich_text'][0]['plain_text']
        }
    pp.pprint(output)
'''