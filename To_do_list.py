class ToDoList:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(self.size)]

    def hash(self, key):
        h = 0
        for x in key:
            h += ord(x)
        return h % self.size

    def add_task(self, tasks, date):
        h = self.hash(tasks)
        if self.data[h] is None:
            self.data[h] = [{"tasks": tasks, "date": date, "completed": False}]
        else:
            self.data[h].append({"tasks": tasks, "date": date, "completed": False})

    def display_all_tasks(self):
        return [x for x in self.data if x is not None]

    def mark_task_as_completed(self, tasks):
        for task in self.data:
            if task is not None:
                for x in task:
                    if x["tasks"] == tasks:
                        x["completed"] = True
                        return True
        return False

    def remove_completed_tasks(self):
        self.data = [[x for x in task if not x["completed"]] if task is not None else None for task in self.data]
        return True

    def sort_tasks_by_name(self):
        for tasks in self.data:
            if tasks is not None:
                tasks.sort(key=lambda x: x["tasks"])

    def sort_tasks_by_due_date(self):
        for tasks in self.data:
            if tasks is not None:
                tasks.sort(key=lambda x: x["date"])

    def sort_tasks_by_completion(self):
        for tasks in self.data:
            if tasks is not None:
                tasks.sort(key=lambda x: x["completed"])

# Example usage:

todo_list = ToDoList(size=100)

# Add tasks...

todo_list.add_task("Read a book", "2022-01-31")
todo_list.add_task("Write code", "2022-02-15")
todo_list.add_task("Exercise", "2022-01-20")

print(todo_list.display_all_tasks())


# Display unsorted tasks
print("Unsorted Tasks:")
print(todo_list.display_all_tasks())

# Sort tasks by name
todo_list.sort_tasks_by_name()
print("\nSorted Tasks by Name:")
print(todo_list.display_all_tasks())

# Sort tasks by due date
todo_list.sort_tasks_by_due_date()
print("\nSorted Tasks by Due Date:")
print(todo_list.display_all_tasks())

# Sort tasks by completion status
todo_list.sort_tasks_by_completion()
print("\nSorted Tasks by Completion Status:")
print(todo_list.display_all_tasks())
