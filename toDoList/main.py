import tasks as tk

while True:

    op = int(input("Select the option to run: \n 1 - Add new task \n 2 - Remove task \n 3 - View all tasks  \n 4 - EXIT \n"))

    match op:

        case 1:
            while True:
             qtdAdd = input("Inform how many task will be add: \n")
             if tk.checkValue(qtdAdd) == "":
              print("Invalid value!")
             else:
              qtdAdd = tk.checkValue(qtdAdd)
              for i in range(qtdAdd):
               tk.add_task(input("Inform the task to add: "))
              break
                
        case 2:
            while True:
             qtdRemove = input("Inform how many task will be remove: \n")
             if tk.checkValue(qtdRemove) == "":
               print("Invalid value!")
             else:
              qtdRemove = tk.checkValue(qtdRemove)
              if qtdRemove > len(tk.tasks):
               print("The task quantity informed is higher than list total!")
              else:
               tk.view_tasks()
               for i in range(qtdRemove):
                tk.remove_task(input("Inform the task to remove: "))
              break
        case 3:
            tk.view_tasks()
        case 4:
            break
        case __:
            print("Invalid option!")