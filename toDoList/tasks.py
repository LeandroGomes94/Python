tasks = []

def add_task(task):

    tasks.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("This task is not in the list")

def view_tasks():
    if len(tasks) <= 0:
        print("No tasks found!")
    else:
        print("Tasks: \n")
        for task in tasks:
            print("- " + task + "\n")

def checkValue(n):
   
   try:
      n = int(n)
      return n
   except:
      return ""