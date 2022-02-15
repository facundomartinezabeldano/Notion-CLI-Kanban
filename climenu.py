from InquirerPy import inquirer
from black import main
import menues as mn
import os
from colorama import Fore

with open("src/kanbanlogo.txt", "r", encoding="utf8") as f:
    for line in f:
        print(Fore.GREEN + line.rstrip())
  
def main_menu():
    if (os.stat("src/userdata.txt").st_size == 0):
        with open("src/userdata.txt","w+") as data:
            api_key = inquirer.secret(message="Please provide your API key:").execute()
            database_id = inquirer.text(message="Please provide your database id:").execute()
            data.write(api_key)
            data.write("\n") #I'm way too lazy to google how to do this in one line of code feel free to fork here king / queen
            data.write(database_id)
    
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