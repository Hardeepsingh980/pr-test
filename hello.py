class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Added task:", task)

    def list_tasks(self):
        if not self.tasks:
            print("task to show")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print("Removed task:", removed_task)
        else:
            print("Invalid task number!")

def main():
    todo = ToDoList()
    while True:
        print("\nTodo List Commands:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Exit")
        command = input("Enter command: ")
        
        if command == "1":
            task = input("Enter a task to add: ")
            todo.add_task(task)
        elif command == "2":
            todo.list_tasks()
        elif command == "3":
            task_number = int(input("Enter task number to remove: "))
            todo.remove_task(task_number)
        elif command == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
