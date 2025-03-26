import json
import uuid
from datetime import datetime, timedelta


def is_exists(todos, task_id):
    return next((todo for todo in todos if todo['id'] == task_id), None)


def save_todos(todos):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(todos, file, indent=4) 
    except Exception as e:
        print("Error while saving todos:", e)


def load_todo():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_todo(todos):
    name = input("Enter Task Name: ")
    priority = input("Priority (Low, Medium, High): ").capitalize()
    if priority not in ['Low', 'Medium', 'High']:
        print("❌ Invalid Priority! Please enter 'Low', 'Medium', or 'High'.")
        return

    days_left = int(input("How many days to complete the task? "))
    due_date = datetime.now() + timedelta(days=days_left)
    due_date_str = due_date.strftime("%Y-%m-%d")

    payload = {
        'id': uuid.uuid4().hex,
        'name': name,
        'status': 'Pending',
        'due_date': due_date_str,
        'priority': priority
    }

    todos.append(payload)
    save_todos(todos)
    print("✅ Todo Added Successfully!")


def view_all_todo(todos):
    pending_tasks = sorted(
        [todo for todo in todos if todo['status'] == 'Pending'],
        key=lambda x: ('High Medium Low'.index(x['priority']), x['due_date'])
    )
    completed_tasks = sorted(
        [todo for todo in todos if todo['status'] == 'Completed'],
        key=lambda x: ('High Medium Low'.index(x['priority']), x['due_date'])
    )

    print("\n📌 PENDING TASKS:")
    if pending_tasks:
        for todo in pending_tasks:
            print(f"{todo['id']} | {todo['name']} | {todo['status']} | {todo['due_date']} | {todo['priority']}")
    else:
        print("No pending tasks.")

    print("\n✅ COMPLETED TASKS:")
    if completed_tasks:
        for todo in completed_tasks:
            print(f"{todo['id']} | {todo['name']} | {todo['status']} | {todo['due_date']} | {todo['priority']}")
    else:
        print("No completed tasks.")


def update_todo(todos):
    task_id = input("Enter Task ID to Update: ")
    task = is_exists(todos, task_id)

    if task:
        new_name = input("Enter New Task Name: ")
        task['name'] = new_name
        save_todos(todos)
        print("✅ Task Updated Successfully!")
    else:
        print("❌ Task not found!")


def mark_as_done_todo(todos):
    task_id = input("Enter Task ID to Mark as Completed: ")
    task = is_exists(todos, task_id)

    if task:
        task['status'] = 'Completed'
        save_todos(todos)
        print("✅ Task Marked as Completed!")
    else:
        print("❌ Task not found!")


def delete_todo(todos):
    task_id = input("Enter Task ID to Delete: ")
    task = is_exists(todos, task_id)

    if task:
        updated_todos = [todo for todo in todos if todo['id'] != task_id]
        save_todos(updated_todos)
        print("✅ Task Deleted Successfully!")
        return updated_todos
    else:
        print("❌ Task not found!")
        return todos


def main():
    todos = load_todo()
    while True:
        print("\n📌 Welcome to To-Do List Manager! ")
        print("1️⃣ Add New Task")
        print("2️⃣ View All Tasks")
        print("3️⃣ Update Task")
        print("4️⃣ Mark Task as Done")
        print("5️⃣ Delete Task")
        print("6️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_all_todo(todos)
        elif choice == '3':
            update_todo(todos)
        elif choice == '4':
            mark_as_done_todo(todos)
        elif choice == '5':
            todos = delete_todo(todos)  
        elif choice == '6':
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == '__main__':
    main()