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


# Add Tasks
def add_task():
    user = input("Enter user: ")
    task = input("Enter task: ")

    while True:
        time_str = input("Enter time (YYYY-MM-DD HH:MM:SS): ")
        try:
            datetime.datetime.strptime(time_str, "%d-%m-%Y %H:%M:%S")
            break
        except:
            print("❌ Invalid format! Try again.")
            print("Format: DD-MM-YYYY HH:MM:SS (e.g. 22-03-2026 20:25:00)")

    repeat = input("Repeat (none/daily): ").lower()
    if repeat not in ["none", "daily"]:
        repeat = "none"

    tasks = load_tasks()

    tasks.append({
        "user": user,
        "task": task,
        "time": time_str,
        "repeat": repeat,
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

    print("\n📋 Task List:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['user']} - {t['task']} at {t['time']} ({t['repeat']})")


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


# SCHEDULER
def run_scheduler():
    while True:
        tasks = load_tasks()
        now = datetime.datetime.now()

        updated_tasks = []

        for t in tasks:
            task_time = datetime.datetime.strptime(t["time"], "%d-%m-%Y %H:%M:%S")

            # Trigger only once
            if not t.get("done", False) and now >= task_time:
                print(f"\n🔔 {t['user']} → {t['task']}")

                if t["repeat"] == "daily":
                    new_time = task_time + datetime.timedelta(days=1)
                    t["time"] = new_time.strftime("%d-%m-%Y %H:%M:%S")
                    t["done"] = False
                else:
                    t["done"] = True

            updated_tasks.append(t)

        save_tasks(updated_tasks)
        time.sleep(1)


# MENU
def menu():
    while True:
        print("\n===== TASK SCHEDULER =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Main
if __name__ == "__main__":
    # Start scheduler thread
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

    menu()