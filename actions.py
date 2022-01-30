import pprint
from notion_client import Client
from notion_client.helpers import get_id
notion = Client(auth="secret_eb1BDBMm4ZTVPqgWCJKnNapjjdPCJLQogDz4svIV1lI")


def edit_task_action(task):
    # edit the selected task
    return


def list_tasks_action():
    query = notion.databases.query(
        database_id="63cd54d3b2254b02b9f258c52e38400a")['results']
    urls = [element['url'] for element in query]
    res = []
    for url in urls:
        p = notion.pages.retrieve(get_id(url))
        r = {
            'title': p['properties']['Task']['title'][0]['text']['content'],
            'status': p['properties']['Status']['multi_select'][0]['name'],
            'due-date': p['properties']['Due date']['rich_text'][0]['text']['content'],
            'short-description': p['properties']['Short Description']['rich_text'][0]['text']['content'],
            'id': get_id(url)
        }
        res.append(r)
    pprint.pprint(query)
    return res


def delete_task_action(id):
    notion.blocks.delete(block_id=id)
    return


def set_status_action(task_id, status):
    return


def add_task_action():
    notion.databases.retrieve('63cd54d3b2254b02b9f258c52e38400a')
    notion.pages.create(
        parent={'database_id': '63cd54d3b2254b02b9f258c52e38400a'},
        properties={
            'Short Description': {'text': {
                'content': 'POROOOOOOOOOOOOONGAAAAAAAAAAA'
            }},
            'Status': {
                'multi_select': [
                    {
                        'name': 'B'
                    }
                ]
            },
            'Due date': {'title': [
                {
                    'type': 'text',
                    'text': {
                        'content': 'DIIIIIIIIIIIIICK'
                    }
                }
            ]},
            'Task': {'id': 'title', 'name': 'Task', 'type': 'title', 'title': {}}}
    )

    return


