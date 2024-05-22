# Define a to-do list
to_do_list = []

def add_task():
  """
  This function adds a new task to the to-do list.
  """
  new_task = input("Enter a new task: ")
  to_do_list.append(new_task)
  print(f"Task '{new_task}' added successfully!")

def view_tasks():
  """
  This function displays all the tasks in the to-do list.
  """
  if len(to_do_list) == 0:
    print("There are no tasks in the list.")
  else:
    print("Your to-do list:")
    for i, task in enumerate(to_do_list):
      print(f"{i+1}. {task}")

def mark_complete():
  """
  This function allows the user to mark a task as completed.
  """
  if len(to_do_list) == 0:
    print("There are no tasks to mark complete.")
  else:
    view_tasks()
    try:
      task_number = int(input("Enter the number of the task to mark complete: ")) - 1
      if task_number >= 0 and task_number < len(to_do_list):
        del to_do_list[task_number]
        print("Task marked complete!")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  """
  This function is the main loop of the program.
  """
  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      mark_complete()
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
# Define a to-do list
to_do_list = []

def add_task():
  """
  This function adds a new task to the to-do list.
  """
  new_task = input("Enter a new task: ")
  to_do_list.append(new_task)
  print(f"Task '{new_task}' added successfully!")

def view_tasks():
  """
  This function displays all the tasks in the to-do list.
  """
  if len(to_do_list) == 0:
    print("There are no tasks in the list.")
  else:
    print("Your to-do list:")
    for i, task in enumerate(to_do_list):
      print(f"{i+1}. {task}")

def mark_complete():
  """
  This function allows the user to mark a task as completed.
  """
  if len(to_do_list) == 0:
    print("There are no tasks to mark complete.")
  else:
    view_tasks()
    try:
      task_number = int(input("Enter the number of the task to mark complete: ")) - 1
      if task_number >= 0 and task_number < len(to_do_list):
        del to_do_list[task_number]
        print("Task marked complete!")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  """
  This function is the main loop of the program.
  """
  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      mark_complete()
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__== "__main__":
  main()
