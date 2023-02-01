from datetime import date
import pickle
from collections import UserDict


class ToDoList(UserDict):
    def __init__(self):
        try:
            with open('data.txt', 'rb') as file:
                self.data = pickle.load(file)
        except:
            self.data = {}
    
    def save_data(self):
        if self.data:
            with open("data.txt", "wb") as file:
                data_base = pickle.dump(self.data, file)

    # self.data = {'name1': [], 'name2':[]}
    def add_todo(self, name):
        self.data[name] = []

    def del_todo(self, name):
        del self.data[name]

    def change_todo_name(self, name, new_name):
        self.data[new_name] = self.data.pop(name)
        print('||-----',self.data)


class Task:
    def __init__(self, task_name, note, status=False, date_add=str(date.today())):
        self.task_name = task_name
        self.note = note
        self.status = status
        self.date_add = date_add
    
    







