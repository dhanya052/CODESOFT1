"""
TASK 1 - To-Do List Application
CodSoft Python Programming Internship

A command-line To-Do List app that lets a user create, view, update,
mark complete, and delete tasks. Tasks are saved to a local JSON file
(tasks.json) so the list persists between runs.

Run:
    python todo.py
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    """Load tasks from the JSON data file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Persist the current task list to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return
    due = input("Due date (YYYY-MM-DD) or leave blank: ").strip()
    task = {
        "id": (max([t["id"] for t in tasks], default=0) + 1),
        "title": title,
        "due": due if due else None,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {title}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!\n")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for t in tasks:
        status = "[X]" if t["done"] else "[ ]"
        due = f" (due {t['due']})" if t.get("due") else ""
        print(f"{t['id']:>3}. {status} {t['title']}{due}")
    print()


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task number to mark complete: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task #{task_id} marked as complete.\n")
            return
    print("Task not found.\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task number to update: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            new_title = input(f"New title (leave blank to keep '{t['title']}'): ").strip()
            if new_title:
                t["title"] = new_title
            new_due = input("New due date YYYY-MM-DD (leave blank to keep current): ").strip()
            if new_due:
                t["due"] = new_due
            save_tasks(tasks)
            print(f"Task #{task_id} updated.\n")
            return
    print("Task not found.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Task #{task_id} deleted.\n")
            return
    print("Task not found.\n")


def print_menu():
    print("=" * 32)
    print("       TO-DO LIST MENU")
    print("=" * 32)
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-6.\n")


if __name__ == "__main__":
    main()
