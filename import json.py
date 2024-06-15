import json
from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'deadline': self.deadline,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict['description'], task_dict['deadline'])
        task.completed = task_dict['completed']
        return task

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task.from_dict(task) for task in tasks_data]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
        tasks.append(Task(description, deadline))
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task.completed else "Incomplete"
        print(f"{index}. {task.description} - {task.deadline} - {status}")

def update_task(tasks):
    task_number = int(input("Enter task number to update: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task.description = input("Enter new description: ")
        deadline = input("Enter new deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            task.deadline = deadline
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    task_number = int(input("Enter task number to remove: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    task_number = int(input("Enter task number to mark complete: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1].completed = True
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Mark Task Complete")
        print("6. Save and Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            mark_task_complete(tasks)
        elif choice == '6':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()