import json

# Define the Task class
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✔" if self.completed else "✖"
        return f"[{status}] {self.title} ({self.category}) - {self.description}"

# Helper function to convert Task objects to a serializable dictionary
def task_to_dict(task):
    return {
        'title': task.title,
        'description': task.description,
        'category': task.category,
        'completed': task.completed
    }

# Helper function to create a Task object from a dictionary
def dict_to_task(data):
    task = Task(data['title'], data['description'], data['category'])
    task.completed = data['completed']  # Restore the completed status
    return task

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task_to_dict(task) for task in tasks], f, indent=4)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            return [dict_to_task(data) for data in tasks_data]
    except FileNotFoundError:
        return []

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))
            save_tasks(tasks)  # Save immediately after adding
            print("Task added.")

        elif choice == '2':
            print("\nTasks:")
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_number = int(input("Enter the task number to mark as completed: "))
            if 0 < task_number <= len(tasks):
                tasks[task_number - 1].mark_completed()
                save_tasks(tasks)  # Save immediately after marking as completed
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            display_tasks(tasks)
            task_number = int(input("Enter the task number to delete: "))
            if 0 < task_number <= len(tasks):
                tasks.pop(task_number - 1)
                save_tasks(tasks)  # Save immediately after deleting
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
