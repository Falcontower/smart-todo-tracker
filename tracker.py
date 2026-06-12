import json
import os

# The file where our tasks will be saved
TASKS_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file, or return an empty list if the file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("\n📝 Your to-do list is empty!")
        return
    
    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "❌ Pending"
        print(f"{index}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== SMART TRACKER MENU ===")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Mark Task as Complete")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        
        elif choice == "2":
            title = input("Enter the task name: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print(f"👍 Added: '{title}'")
        
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("\nEnter the number of the task you finished: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["completed"] = True
                        save_tasks(tasks)
                        print("🎉 Task marked as complete!")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "4":
            print("\nGoodbye! Stay productive! 🚀")
            break
        else:
            print("Invalid choice, please pick 1, 2, 3, or 4.")

# This tells Python to start running our main program
if __name__ == "__main__":
    main()
