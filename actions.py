import pprint
import requests
from alive_progress import alive_bar
from notion_client import Client
from notion_client.helpers import get_id
import json

user_data = open("src/userdata.json", "r")
user_data_payload = json.load(user_data)
secret = user_data_payload["log_info"]["api_key"]
id = user_data_payload["log_info"]["database_id"]
user_data.close()

notion = Client(auth=secret)


def edit_task_action(task_id, new_parameters):  # TODO
    properties_payload = {"Status": {"multi_select": [{"name": "adsfads"}]}}
    notion.pages.update(page_id=task_id, properties=properties_payload)
    return


def list_tasks_action(showbar=True):
    url = f"https://api.notion.com/v1/databases/{id}/query"
    payload = {"page_size": 100}
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret}",
    }
    response = requests.request("POST", url, json=payload, headers=headers).json()
    clean_payload = {
        "payloads": [],  # payload list
        "ids": [],       # id list
    }
    if showbar:
        with alive_bar(len(response["results"])) as bar:
            for page in response["results"]:
                children = {
                    "Task": page["properties"]["Task"]["title"][0]["text"]["content"],
                    "Status": page["properties"]["Status"]["multi_select"][0]["name"],
                    "Short Description": page["properties"]["Short Description"][
                        "rich_text"
                    ][0]["plain_text"],
                    "Due date": page["properties"]["Due date"]["rich_text"][0][
                        "plain_text"
                    ],
                }
                clean_payload["ids"].append(page["id"])
                clean_payload["payloads"].append(children)
                bar()
        return clean_payload
    for page in response["results"]:
        children = {
            "Task": page["properties"]["Task"]["title"][0]["text"]["content"],
            "Status": page["properties"]["Status"]["multi_select"][0]["name"],
            "Short Description": page["properties"]["Short Description"]["rich_text"][
                0
            ]["plain_text"],
            "Due date": page["properties"]["Due date"]["rich_text"][0]["plain_text"],
        }
        clean_payload["ids"].append(page["id"])
        clean_payload["payloads"].append(children)

    return clean_payload


def delete_task_action(id_block):
    notion.blocks.delete(block_id=id_block)
    return


def set_status_action(task_id, status):
    p = {
        "Status": {
            "id": "sHE%5E",
            "multi_select": [{"name": status}],
            "type": "multi_select",
        }
    }
    notion.pages.update(page_id=task_id, properties=p)
    return


def add_task_action(request) -> None:
    task_payload = {
        "Due date": {
            "id": "~ePg",
            "rich_text": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": request["Due date"],
                    "text": {"content": request["Due date"], "link": None},
                    "type": "text",
                }
            ],
            "type": "rich_text",
        },
        "Short Description": {
            "id": "DEgC",
            "rich_text": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": request["Description"],
                    "text": {"content": request["Description"], "link": None},
                    "type": "text",
                }
            ],
            "type": "rich_text",
        },
        "Status": {
            "id": "sHE%5E",
            "multi_select": [{"name": request["Status"]}],
            "type": "multi_select",
        },
        "Task": {
            "id": "title",
            "title": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": request["Title"],
                    "text": {"content": request["Title"], "link": None},
                    "type": "text",
                }
            ],
            "type": "title",
        },
    }

    # To see the database schema notion.databases.retrieve(id)
    notion.pages.create(
        parent={"database_id": id},
        properties=task_payload,
    )
    print(
        f'Task {request["Title"]} has been successfully added to Kanban with status: {request["Status"]} ✔ '
    )
    return
