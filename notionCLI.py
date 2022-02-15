from InquirerPy import inquirer
from black import main
import menues as mn
import os
from colorama import Fore

with open("src/kanbanlogo.txt", "r", encoding="utf8") as f:
    for line in f:
        print(Fore.GREEN + line.rstrip())


def main_menu():
    if os.stat("src/userdata.json").st_size == 0:
        data = open("src/userdata.txt", "w+")
        api_key = inquirer.secret(message="Please provide your API key:").execute()
        database_id = inquirer.text(message="Please provide your database id:").execute()
        data.write(f"{api_key}\n{database_id}")
        data.close()

    l = [
        "Add task 📜 ",
        "List tasks 🧾 ",
        "Edit task 📝 ",
        "Delete task ❌ ",
        "Set status 🔖 ",
        "Exit 🔚",
        "Clear screen",
    ]

    r = inquirer.fuzzy(message="Select an action to perfom", choices=l).execute()

    options = {
        "Add task 📜 ": mn.add_task_menu,
        "List tasks 🧾 ": mn.list_tasks_menu,
        "Edit task 📝 ": mn.edit_task_menu,
        "Delete task ❌ ": mn.delete_task_menu,
        "Set status 🔖 ": mn.set_status_menu,
        "Exit 🔚": mn.goodbye,
        "Clear screen": mn.clean_screen_and_print_logo,
    }

    options[r]()

    return main_menu()


while True:
    main_menu()
