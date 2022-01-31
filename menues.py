import actions as ac
from InquirerPy import inquirer
from tabulate import tabulate
from colorama import Back , Fore, Style

def add_task_menu():

    t = inquirer.text(message="Add task title").execute()
    d = inquirer.text(message="Add task description").execute()
    du = inquirer.text(message="Add a due date to your task").execute()
    s = inquirer.rawlist(message="Select satus", choices=["Backlog", "To do", "Doing", "Done"]).execute()

    request = {
        "Title": t,
        "Description": d,
        "Due date": du,
        "Status": s,
    }

    ac.add_task_action(request)
    return


def list_tasks_menu():
    print(Fore.GREEN + 'Loading your tasks this may take some time 🕐')
    tasks_payload , task_ids_payload = ac.list_tasks_action()
    h = ["Title","Short Description","Status","Due date"]
    print(tabulate(tasks_payload,headers=h,tablefmt="fancy_grid",numalign="center",stralign="center",showindex=True))
    return task_ids_payload


def edit_task_menu(ls):
    task_name = inquirer.fuzzy(message="Select a task to edit (this will change the entire task)", choices=ls).execute()
    action = ac.edit_task_action(task_name)

    r = {

    }

    return print(f"Task {task_name} was edited successfully")


def delete_task_menu():
    ids = list_tasks_menu()
    task_id = inquirer.number(message="Select a task number to delete ❌ ").execute()
    ac.delete_task_action(ids[int(task_id)])
    print(f"Task number: {task_id} was deleted successfully")
    return


def set_status_menu():
    ls = ac.list_tasks_action()
    task_name = inquirer.rawlist(message="Choose a task to change it's state", choices=ls).execute()
    new_status = inquirer.rawlist(message="Select new status", choices=["Backlog", "To do", "Doing", "Done"])
    action = ac.set_status_action(task_name, new_status)
    return print(f"Task {task_name} has changed to {new_status} successfully")
