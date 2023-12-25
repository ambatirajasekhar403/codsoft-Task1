def add_task(task_list, task):
    if len(task) == 0:
        print('Error: Field is Empty.')
    else:
        task_list.append(task)
        print('Task added successfully!')

def display_tasks(task_list):
    if not task_list:
        print('No tasks found.')
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def delete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        deleted_task = task_list.pop(task_index)
        print(f'Task "{deleted_task}" deleted successfully.')
    else:
        print('Invalid task number.')

def delete_all_tasks(task_list):
    if not task_list:
        print('No tasks to delete.')
    else:
        task_list.clear()
        print('All tasks deleted successfully.')

if __name__ == "__main__":
    tasks = ["Task 1", "Task 2", "Task 3"]

    while True:
        print("\n To-Do List Menu")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Delete All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task name: ")
            add_task(tasks, task)
        elif choice == "2":
            print("Total Tasks in the List :")
            display_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == "4":
            delete_all_tasks(tasks)
        elif choice == "5":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")
