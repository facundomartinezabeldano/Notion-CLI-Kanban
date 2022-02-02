import pprint
from notion_client import Client
from notion_client.helpers import get_id
from numpy import add
from alive_progress import alive_bar
import time
notion = Client(auth="secret_eb1BDBMm4ZTVPqgWCJKnNapjjdPCJLQogDz4svIV1lI")


def edit_task_action(task):
    # edit the selected task
    return


def list_tasks_action(showbar=True):
    query = notion.databases.query(
        database_id="63cd54d3b2254b02b9f258c52e38400a")['results']
    urls = [element['url'] for element in query]
    task_list_payload = []
    task_ids_payload = []

    if(showbar):
        with alive_bar(len(urls)) as bar:
            for url in urls:
                p = notion.pages.retrieve(get_id(url))
                r = [
                    p['properties']['Task']['title'][0]['text']['content'],  # title
                    # Description
                    p['properties']['Short Description']['rich_text'][0]['text']['content'],
                    p['properties']['Status']['multi_select'][0]['name'],  # Status
                    # Due date
                    p['properties']['Due date']['rich_text'][0]['text']['content'],
                ]
                task_list_payload.append(r)
                task_ids_payload.append(get_id(url))
                bar()
            return task_list_payload, task_ids_payload

    for url in urls:
        p = notion.pages.retrieve(get_id(url))
        r = [
            p['properties']['Task']['title'][0]['text']['content'],  # title
            # Description
            p['properties']['Short Description']['rich_text'][0]['text']['content'],
            p['properties']['Status']['multi_select'][0]['name'],  # Status
            p['properties']['Due date']['rich_text'][0]['text']['content'],  # Due date
        ]
        task_list_payload.append(r)
        task_ids_payload.append(get_id(url))

    return task_list_payload, task_ids_payload


def delete_task_action(id):
    notion.blocks.delete(block_id=id)
    return


def set_status_action(task_id, status):
    return


def add_task_action(request) -> None:
    payload = {'Due date': {'id': '~ePg',
                            'rich_text': [{'annotations': {'bold': False,
                                                           'code': False,
                                                           'color': 'default',
                                                           'italic': False,
                                                           'strikethrough': False,
                                                           'underline': False},
                                           'href': None,
                                           'plain_text': request['Due date'],
                                           'text': {'content': request['Due date'], 'link': None},
                                           'type': 'text'}],
                            'type': 'rich_text'},
               'Short Description': {'id': 'DEgC',
                                     'rich_text': [{'annotations': {'bold': False,
                                                                    'code': False,
                                                                    'color': 'default',
                                                                    'italic': False,
                                                                    'strikethrough': False,
                                                                    'underline': False},
                                                    'href': None,
                                                    'plain_text': request['Description'],
                                                    'text': {'content': request['Description'], 'link': None},
                                                    'type': 'text'}],
                                     'type': 'rich_text'},
               'Status': {'id': 'sHE%5E',
                          'multi_select': [{'name': request['Status']}],
                          'type': 'multi_select'},
               'Task': {'id': 'title',
                        'title': [{'annotations': {'bold': False,
                                                   'code': False,
                                                   'color': 'default',
                                                   'italic': False,
                                                   'strikethrough': False,
                                                   'underline': False},
                                   'href': None,
                                   'plain_text': request['Title'],
                                   'text': {'content': request['Title'], 'link': None},
                                   'type': 'text'}],
                        'type': 'title'}}

    # To see the database schema notion.databases.retrieve('63cd54d3b2254b02b9f258c52e38400a')
    notion.pages.create(
        parent={'database_id': '63cd54d3b2254b02b9f258c52e38400a'}, properties=payload)
    return print(f'Task {request["Title"]} has been successfully added to Kanban with status: {request["Status"]} ✔ ')
