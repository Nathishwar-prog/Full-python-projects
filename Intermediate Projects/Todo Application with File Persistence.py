# todo_app.py
import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def display_todos(todos):
    if not todos:
        print("\nNo tasks found. Add some tasks!")
        return
    
    print("\nYour To-Do List:")
    print("-" * 30)
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo['completed'] else " "
        print(f"{i}. [{status}] {todo['task']}")
        print(f"   Priority: {todo['priority']}")
        print(f"   Due: {todo['due_date']}")
        print(f"   Created: {todo['created_at']}")
        print("-" * 30)

def add_todo(todos):
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    
    priority = input("Enter priority (high/medium/low): ").strip().lower()
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Enter priority (high/medium/low): ").strip().lower()
    
    due_date = input("Enter due date (YYYY-MM-DD, leave empty if none): ").strip()
    if not due_date:
        due_date = "No due date"
    
    new_todo = {
        'task': task,
        'priority': priority,
        'due_date': due_date,
        'completed': False,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    todos.append(new_todo)
    save_todos(todos)
    print(f"Task '{task}' added successfully!")

def complete_todo(todos):
    display_todos(todos)
    if not todos:
        return
    
    try:
        task_num = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_num < len(todos):
            todos[task_num]['completed'] = True
            save_todos(todos)
            print(f"Task '{todos[task_num]['task']}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_todo(todos):
    display_todos(todos)
    if not todos:
        return
    
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todos):
            deleted_task = todos.pop(task_num)
            save_todos(todos)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    todos = load_todos()
    
    while True:
        print("\nTo-Do Application")
        print("1. View Todos")
        print("2. Add Todo")
        print("3. Complete Todo")
        print("4. Delete Todo")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            complete_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == '__main__':
    main()
