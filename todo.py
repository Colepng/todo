import argparse

my_parser = argparse.ArgumentParser(description='A todo list')

# Adds something to the todo list
my_parser.add_argument("-a", "--add", metavar='add', type=str, nargs="+", help="Add a todo item")

# Removes something from the todo list
my_parser.add_argument("-r", "--remove", metavar='remove', type=str, help="Remove a todo item")

# Edits something from the todo list
my_parser.add_argument("-e", "--edit", metavar='edit', type=str, nargs="+", help="Edit a todo item")

# Execute the parse_args() method
args = my_parser.parse_args()

# Gets the todo list before the program adds or removes anything
TodoListAtStart = open("todo.txt", "r").read().splitlines()

# Adds something to the todo list
if args.add:
    args.add = " ".join(args.add)
    print(args.add)
    number_of_lines = len(open('todo.txt', 'r').readlines())
    to_write = ('\n' if number_of_lines != 0 else '') + (f"{args.add}")
    open("todo.txt", "a").write(to_write)

# Removes something from the todo list
elif args.remove:
    TodoListEdited = TodoListAtStart
    print("Removing " + args.remove)
    try: 
        TodoListEdited.pop(int(args.remove) - 1)
        open("todo.txt", "w").write("\n".join(TodoListEdited))
        print(f"todo list went from {TodoListAtStart} to {TodoListEdited}")
    except IndexError: 
        if len(TodoListAtStart) == 0:
            print("Todo list empty")
        else:
            print("Specifed item does not exist")

elif args.edit:
    TodoListEdited = TodoListAtStart
    print("Editing " + args.edit[0])
    try:
        TodoListEdited[int(args.edit[0]) - 1] = " ".join(args.edit[1:])
        open("todo.txt", "w").write("\n".join(TodoListEdited))
        print(f"todo list went from {TodoListAtStart} to {TodoListEdited}")
    except IndexError: 
        if len(TodoListAtStart) == 0:
            print("Todo list empty")
        else:
            print("Specifed item does not exist")

# Prints the todo list
else:
    print(open("todo.txt", "r").read())
