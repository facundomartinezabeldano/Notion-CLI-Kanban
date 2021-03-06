from InquirerPy import inquirer
import modules.menues as mn
import json
import os
from colorama import Fore

with open("src/kanbanlogo.txt", "r", encoding="utf8") as f:
    for line in f:
        print(Fore.GREEN + line.rstrip())


def main_menu():

    data_path = os.path.join("src", "userdata.json")
    with open(file=data_path, mode="r", encoding="utf8") as user_data:
        user_data_payload = json.load(user_data)
        if (user_data_payload["log_info"]["api_key"] == "API KEY" or user_data_payload["log_info"]["database_id"] == "DATABASE ID"):
            raise Exception("Please provide your API key and database id")

    l = [
        "Add task ๐ ",
        "List tasks ๐งพ ",
        "Edit task ๐ ",
        "Delete task โ ",
        "Set status ๐ ",
        "Exit ๐",
        "Clear screen",
    ]

    r = inquirer.fuzzy(message="Select an action to perfom", choices=l).execute()

    options = {
        "Add task ๐ ": mn.add_task_menu,
        "List tasks ๐งพ ": mn.list_tasks_menu,
        "Edit task ๐ ": mn.edit_task_menu,
        "Delete task โ ": mn.delete_task_menu,
        "Set status ๐ ": mn.set_status_menu,
        "Exit ๐": mn.goodbye,
        "Clear screen": mn.clean_screen_and_print_logo,
    }

    options[r]()

    return main_menu()


while True:
    main_menu()
