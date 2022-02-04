from InquirerPy import inquirer
import menues as mn
from colorama import Back , Fore, Style

with open("kanbanlogo.txt","r",encoding="utf8") as f:
    for line in f:
            print(Fore.GREEN + line.rstrip())


def main_menu():
    l = ["Add task 📜 ", "List tasks 🧾 ", "Edit task 📝 ",
         "Delete task ❌ ", "Set status 🔖 ", "Exit 🔚"]
    r = inquirer.rawlist(
        message="Select an action to perfom", choices=l).execute()

    options = {
        "Add task 📜 ": mn.add_task_menu,
        "List tasks 🧾 ": mn.list_tasks_menu,
        "Edit task 📝 ": mn.edit_task_menu,
        "Delete task ❌ ": mn.delete_task_menu,
        "Set status 🔖 ": mn.set_status_menu,
        "Exit 🔚": mn.goodbye
    }

    options[r]()

    return main_menu()


while True:
    main_menu()
