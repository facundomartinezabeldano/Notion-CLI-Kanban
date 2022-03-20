from alive_progress import alive_bar
from distutils.fancy_getopt import fancy_getopt
from multiprocessing.connection import wait

from colorama import Fore
from InquirerPy import inquirer
from tabulate import tabulate

import actions as ac
import os
import time


def add_task_menu():

    """Creates a new task"""

    t = inquirer.text(message="Add task title").execute()
    d = inquirer.text(message="Add task description").execute()
    du = inquirer.text(message="Add a due date to your task").execute()
    s = inquirer.rawlist(
        message="Select satus", choices=["Backlog", "To do", "Doing", "Done"]
    ).execute()

    request = {
        "Title": t,
        "Description": d,
        "Due date": du,
        "Status": s,
    }

    ac.add_task_action(request)
    clean_screen_and_print_logo(waiting=True)
    return


def list_tasks_menu(showmenu=True):
    """Calls the API in the actions module and prints it's results"""
    if showmenu:
        print(Fore.GREEN + "Loading your tasks this may take some time 🕐")
        data = ac.list_tasks_action()
        fancy_data = [
            [d["Task"], d["Short Description"], d["Status"], d["Due date"]]
            for d in data["payloads"]
        ]
        h = ["Task", "Short description", "Status", "Due date"]
        print(
            tabulate(
                tabular_data=fancy_data,
                headers=h,
                tablefmt="fancy_grid",
                numalign="center",
                stralign="center",
                showindex=True,
            )
        )
        data_analysis_array = [d[2] for d in fancy_data]
        todos = [i for i in data_analysis_array if i == "To do"]
        dones = [i for i in data_analysis_array if i == "Done"]
        doings = [i for i in data_analysis_array if i == "Doing"]

        print(
            f"{Fore.YELLOW} You have a total of {Fore.BLUE} {len(fancy_data)} {Fore.YELLOW} tasks in your Kanban Board"
        )
        print(f'{Fore.CYAN} You have a total of {len(todos)} tasks in "To do" status')
        print(f'{Fore.RED} You have a total of {len(dones)} tasks in "Done" status')
        print(
            f'{Fore.WHITE} You have a total of {len(doings)} tasks in "Doing" status '
        )
        return data["ids"]
    data = ac.list_tasks_action()
    return data["ids"]


def edit_task_menu():  # TODO
    task_name = inquirer.fuzzy(
        message="Select a task to edit (this will change the entire task)",
        choices="adfadsf",
    ).execute()
    ac.edit_task_action(task_name)
    return print(f"Task {task_name} was edited successfully")


def delete_task_menu():
    tasks_ids = list_tasks_menu()
    task_id = inquirer.number(message="Select a task number to delete ❌ ").execute()
    ac.delete_task_action(tasks_ids[int(task_id)])
    print(f"Task number: {task_id} was deleted successfully")
    clean_screen_and_print_logo(waiting=True)
    return


def set_status_menu():
    ids = list_tasks_menu()
    task_id = inquirer.number(
        message="Choose a task to change it's state",
        max_allowed=len(ids),
        min_allowed=0,
    ).execute()
    new_status = inquirer.rawlist(
        message="Select new status", choices=["Backlog", "To do", "Doing", "Done"]
    ).execute()
    ac.set_status_action(ids[int(task_id)], new_status)
    print(f"Task status changed to => {new_status} successfully 🎉 ")
    clean_screen_and_print_logo(waiting=True)
    return


def goodbye():
    with open(os.path.join("src", "goodbye.txt"), "r", encoding="utf8") as f:
        for line in f:
            print(Fore.GREEN + line.rstrip())
    return exit()


def print_logo():
    with open(os.path.join("src", "kanbanlogo.txt"), "r", encoding="utf8") as f:
        for line in f:
            print(Fore.GREEN + line.rstrip())
    return


def clean_screen_and_print_logo(waiting=False):
    if waiting:
        print("Your screen will be clear in 3s")
        with alive_bar(total=5) as bar:
            for i in range(0, 3):
                time.sleep(1)
                bar()
        os.system("cls" if os.name == "nt" else "clear")
        return print_logo()

    os.system("cls" if os.name == "nt" else "clear")
    return print_logo()
