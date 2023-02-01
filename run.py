import core
import os
os.system('clear')

TODOLIST = core.ToDoList()

# menu functions
def add_todo(name):
    TODOLIST.add_todo(name)


def delete_todo(name):
    TODOLIST.del_todo(name)


def change_todo_name(args):
    args = args.split(' ')
    name, new_name = args[0], args[1]
    TODOLIST.change_todo_name(name=name, new_name=new_name)


def task_menu(name):
    print(f'name is <{name}>')
    if name not in TODOLIST.data:
        return 'this name not in todo'
    global in_tasks, todo_name
    todo_name = name
    in_tasks = True


def add_task(args):
    args = args.split('|')
    task_name, note = args[0], args[1]
    task = core.Task(task_name=task_name, note=note)
    TODOLIST.data[todo_name].append(task)


def change_status(task_name):
    for i in TODOLIST.data[todo_name]:
        if i.task_name == task_name:
            if i.status:
                i.status = False
            else:
                i.status = True
        continue


def del_task(task_name):
    for i in TODOLIST.data[todo_name]:
        if i.task_name == task_name:
            print('removing\n'*20)
            TODOLIST.data[todo_name].remove(i)
        continue


def show_task(name):
    for i in TODOLIST.data[todo_name]:
        if i.task_name.strip() == name.strip():
            print('|', i.note.strip())
            input(' ')
        else:
            continue
            

commands = {
    'add todo' : ['[ name ]', add_todo],
    'del todo' : ['[ name ]', delete_todo],
    'change todo name' : ['[ name ] [ new name ]', change_todo_name],
    'go to' : ['[ name ]', task_menu],
}

commands_task = {
    'add task' : ['[task name] | [note]', add_task],
    'del task' : ['[task name]', del_task],
    'show task' : ['[task name]', show_task],
    'change status' : ['[task name]', change_status],
}



def main():
    global in_tasks
    in_menu = True
    in_tasks = False 

    while in_menu:
        os.system('clear')
        print('_'*40)
        print("| Hello to your ToDoList's\n|___\n|")

        if not TODOLIST:
            print('| U dont have any ToDo')
        else:
            for i in TODOLIST.data:
                print(f'| * {i}')
        
        
        print('|__\n| Commands:\n|')
        for i,j in commands.items():
            print(f'| - {i.capitalize()} - {j[0]}')
        print('| - Exit')
        print('|__')
        us_command = input('| Chose the command: ').lower()
        if us_command in ('q','exit'):
            TODOLIST.save_data()
            break
        args = input('| :: ').rstrip()

        try:
            print('handler')
            handler = commands[us_command][1]
            print(handler)
            handler(args)
        except:
            print('|| ERROn\n'*40)
            continue
    
        
        
        while in_tasks:
            os.system('clear')
            print('_'*40)
            print("| Hello to your tasks's\n|___\n|")

            if TODOLIST.data[todo_name] == []:
                print('| U dont have any tasks')
            else:
                my_list = [[],[]]
                for i in TODOLIST.data[todo_name]:
                    if i.status == False:
                        my_list[1].append('| ø {:<80} {:>10}'.format(i.task_name, i.date_add))
                    else:
                        my_list[0].append('| ˚ {:<80} {:>10}'.format(i.task_name, i.date_add))

                # uncomplete
                for i in my_list[1]:
                    print(i)

                # complete
                print('|\n|-- Completed')
                for i in my_list[0]:
                    print(i)
                    
            
            print('|__\n|\n| Commands:\n|')
            for i,j in commands_task.items():
                print(f'| - {i.capitalize()} - {j[0]}')
            print('| - Back')
            print('|__')
            us_command = input('| Chose the command: ').lower()
            if us_command in ('q','exit', 'back'):
                TODOLIST.save_data()
                in_tasks = False
                break

            args = input('| :: ').rstrip()
            try:
                handler = commands_task[us_command][1]
                handler(args)
            except:
                continue


            





if __name__ == "__main__":
    main()