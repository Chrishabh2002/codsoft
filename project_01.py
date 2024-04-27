class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks!")
        else:
            for i, task in enumerate(self.tasks, start=1):                    # using enumerate to add a number to each task
                status = "Complete" if task["completed"] else "Incomplete"
                print(f"{i}. {task['task']} - {status}")

    def mark_complete(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
        else:
            print("Invalid task index!")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index!")


def main():

    todo_list = TodoList()

    # Display menu options and process user input
    while True:
        print("1. Add Task \n")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
