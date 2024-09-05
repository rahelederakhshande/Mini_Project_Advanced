from C_Task import * 

class Todolost_manager:
    def __init__(self):
        self.task={}

    def create_task(self, id_i, name):
        new_task = Task(id_i, name)
        return new_task
    
    def add_task(self, task):
        if task.id_i not in self.task:
            self.task[task.id_i] = task
            print("added!")
        else:
            print("Exists!")

    def remove_task(self, id_i):
        if id_i in self.task:
            del self.task[id_i]
            print("removed!")
        else:
            print("not found!")

    def display_task(self):
        for task1 in self.task.values():
            print(task1)

    def edit_task(self, id_i):
        if id_i in self.task:
            new_task = input("new task: ")
            self.task[id_i].name = new_task or self.task[id_i].name
            print("Edited!")
        else:
            print("not found!")
            
    def search_name(self,name):
        flag=False
        for task in self.task.values():
            if task.name == name:
                print(f"Yes It's found:{task}")
                flag = True
        if not flag:
            print("Not Found!,Please Try Again Later.")
        
    def search_id(self,id_i):
        
        if id_i in self.task:
            print(f"Found:{self.task[id_i]} ")
            
        else:
            print("Not Found!")

    
    def search_done(self):
        done_tasks = [task for task in self.task.values() if task.state]
        for task in done_tasks:
            print(task)


    def search_undone(self):
        undone_tasks = [task for task in self.task.values() if not task.state]
        for task in undone_tasks:
            print(task)