import actions as ac
from InquirerPy import inquirer


def add_task_menu():

    t = inquirer.text(message="Add task title").execute()
    d = inquirer.text(message="Add task description").execute()
    p = inquirer.text(message="Add a due date to your task").execute()
    s = inquirer.rawlist(message="Select satus", choices=[
                         "Backlog", "To do", "Doing", "Done"]).execute()

    r = {
        "Title": t,
        "Description": d,
        "Due date": p,
        "Status": s,
    }

    ac.add_task_action(r)
    return


def list_tasks_menu():
    objs = ac.list_tasks_action()
    res = inquirer.rawlist(message="Your tasks here", choices=[
                           i['title'] for i in objs]).execute()
    return


def edit_task_menu(ls):
    task_name = inquirer.fuzzy(
        message="Select a task to edit (this will change the entire task)", choices=ls).execute()
    action = ac.edit_task_action(task_name)

    r = {

    }

    return print(f"Task {task_name} was edited successfully")


def delete_task_menu():
    objs = ac.list_tasks_action()
    decisions = {i['title']: i['id'] for i in objs}
    task_name = inquirer.rawlist(message="Select a single task to delete ❌ ", choices=[
                                 i['title'] for i in objs]).execute()
    ac.delete_task_action(decisions[task_name])
    print(f"Task {task_name} was deleted successfully")
    return


def set_status_menu():
    ls = ac.list_tasks_action()
    task_name = inquirer.rawlist(
        message="Choose a task to change it's state", choices=ls).execute()
    new_status = inquirer.rawlist(message="Select new status", choices=[
                                  "Backlog", "To do", "Doing", "Done"])
    action = ac.set_status_action(task_name, new_status)
    return print(f"Task {task_name} has changed to {new_status} successfully")
