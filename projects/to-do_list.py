class Task:
    def __init__(self, title, description):
        self.title = title
        self.desc = description

    def __str__(self):
        return f"{self.title}: {self.desc}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task: {title}, has been added.")

    def remove_task(self, title):
        for i, task in enumerate(self.tasks):
            if task.title == title:
                del self.tasks[i]
                print(f"Task: {title}, has been removed.")
                return
        print(f"Task: {title}, not found. Nothing to remove.")

    def remove_task_by_index(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task: {removed_task.title}, has been removed.")
        else:
            print(f"Task: {index}, not found. Nothing to remove.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i} - {task}")
                
    def clear_tasks(self):
        if not self.tasks:
            print("Your to-do list is already empty.")
        else:
            self.tasks.clear()
            print("All tasks have been cleared.")

todo_list = ToDoList()