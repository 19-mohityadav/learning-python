import json
import time
import datetime
import threading
import os

FILE = "tasks.json"


# Load Tasks
def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Save Tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# Add Task
def add_task():
    user = input("Enter user: ")
    task = input("Enter task: ")

    while True:
        time_str = input("Enter time (DD-MM-YYYY HH:MM:SS): ")
        try:
            datetime.datetime.strptime(time_str, "%d-%m-%Y %H:%M:%S")
            break
        except:
            print("❌ Invalid format! Use: 22-03-2026 20:25:00")

    repeat = input("Repeat (none/daily/weekly): ").lower()
    if repeat not in ["none", "daily", "weekly"]:
        repeat = "none"

    priority = input("Priority (low/medium/high): ").lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"

    tasks = load_tasks()

    tasks.append({
        "user": user,
        "task": task,
        "time": time_str,
        "repeat": repeat,
        "priority": priority,
        "done": False
    })

    save_tasks(tasks)
    print("✅ Task added successfully")


# Show Tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    # Sort by time safely
    def get_time(t):
        try:
            return datetime.datetime.strptime(t["time"], "%d-%m-%Y %H:%M:%S")
        except:
            return datetime.datetime.now()

    tasks.sort(key=get_time)

    print("\n📋 Task List:")
    for i, t in enumerate(tasks):
        priority = t.get("priority", "medium").upper()
        print(f"{i+1}. [{priority}] {t['user']} - {t['task']} at {t['time']} ({t['repeat']})")


# Search Task
def search_task():
    name = input("Enter user to search: ")
    tasks = load_tasks()

    found = False
    for t in tasks:
        if t["user"].lower() == name.lower():
            print(f"🔍 [{t.get('priority','medium')}] {t['user']} - {t['task']} at {t['time']}")
            found = True

    if not found:
        print("❌ No tasks found")


# Delete Task
def delete_task():
    tasks = load_tasks()
    show_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Deleted: {removed['task']}")
        else:
            print("❌ Invalid number")

    except:
        print("❌ Invalid input")


# Time Remaining
def time_remaining():
    tasks = load_tasks()
    now = datetime.datetime.now()

    print("\n⏳ Time Remaining:")
    for t in tasks:
        try:
            task_time = datetime.datetime.strptime(t["time"], "%d-%m-%Y %H:%M:%S")
            diff = task_time - now

            if diff.total_seconds() > 0:
                print(f"{t['task']} → {diff}")
            else:
                print(f"{t['task']} → Time Passed")
        except:
            print(f"{t['task']} → Invalid time format")


# Scheduler
def run_scheduler():
    while True:
        tasks = load_tasks()
        now = datetime.datetime.now()

        updated_tasks = []

        for t in tasks:
            try:
                task_time = datetime.datetime.strptime(t["time"], "%d-%m-%Y %H:%M:%S")
            except:
                updated_tasks.append(t)
                continue

            if not t.get("done", False) and now >= task_time:
                print(f"\n🔔 [{t.get('priority','medium')}] {t['user']} → {t['task']}")

                if t["repeat"] == "daily":
                    new_time = task_time + datetime.timedelta(days=1)
                    t["time"] = new_time.strftime("%d-%m-%Y %H:%M:%S")

                elif t["repeat"] == "weekly":
                    new_time = task_time + datetime.timedelta(days=7)
                    t["time"] = new_time.strftime("%d-%m-%Y %H:%M:%S")

                else:
                    t["done"] = True

            updated_tasks.append(t)

        save_tasks(updated_tasks)
        time.sleep(1)


# Menu
def menu():
    while True:
        print("\n===== TASK SCHEDULER (LEVEL 2) =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Search by User")
        print("5. Time Remaining")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            search_task()
        elif choice == "5":
            time_remaining()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Main
if __name__ == "__main__":
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

    menu()