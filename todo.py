tasks =[] #This list will store our tasks

while True:
  print("\nTo-Do List App")
  print("1. Add Task")
  print("2. View Task")
  print("3. Remove Task")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice =="1":
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'"{task}" has been added.')

  elif choice =="2":
    if not tasks:
      print("No tasks available.")
    else:
      print("\nYour To-Do List:")
      for index, task in enumerate(tasks, 1):
        print(f"{index}.{task}")

  elif choice == "3":
    if not tasks:
      print("No tasks to remove.")
    else:
      print("n\Your To-Do List:")
      for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

      try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
          removed_task = tasks.pop(task_number - 1)
          print(f'"{removed_task}" has been removed.')
        else:
          print("Invalid number. Please try again.")
      except ValueError:
        print("please enter a valid number.")

  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. please enter a number between 1 and 4.")