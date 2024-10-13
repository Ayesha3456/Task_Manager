Personal To-Do List Application
Overview
This Personal To-Do List Application allows users to manage tasks through a command-line interface. It provides essential task management features, stores tasks locally in a tasks.json file, and ensures tasks persist between sessions.

Features
Add Task: Users can add tasks with a title, description, and category (e.g., Work, Personal, Urgent).
View Tasks: Displays all tasks with their title, category, description, and completion status.
Mark Task as Completed: Marks tasks as completed, with a visual indicator.
Delete Task: Allows users to delete tasks from the list.
Automatic Saving: Tasks are automatically saved to tasks.json after every change.
Persistent Storage: Tasks are loaded from the tasks.json file upon restarting the application.
Requirements
Python 3.x
No external dependencies are needed (json is a built-in module).
Installation
Clone or download the repository to your local machine.
Navigate to the project directory.
bash
Copy code
cd /path/to/todo_app
Usage
Run the application:
bash
Copy code
python todo.py
Main Menu Options:

markdown
Copy code
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Adding a Task: Choose option 1 and enter task details (title, description, and category).

Viewing Tasks: Select option 2 to see all tasks, including their status and details.

Marking Task as Completed: Select option 3 to mark a task as done.

Deleting a Task: Choose option 4 to remove a task from the list.

Exiting the Application: Choose option 5 to save changes and close the program.

File Structure
bash
Copy code
/todo_app
 ├── todo.py       # Main application script
 ├── tasks.json    # JSON file to store tasks (auto-generated)
 └── README.md     # Documentation
Task Format
Tasks are stored in tasks.json with the following structure:

json
Copy code
{
    "title": "Sample Task",
    "description": "Sample description",
    "category": "Work",
    "completed": false
}
Troubleshooting
File Not Found: If tasks.json is missing, it will be created the first time a task is added.
Invalid Input: Enter valid numbers when selecting tasks to complete or delete.