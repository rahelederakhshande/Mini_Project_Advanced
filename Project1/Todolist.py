from task import * 
class Todolost_manager:
    def __init__(self):
        self.task={}
    def create_task(self, id_i, title, status):
        new_task = Task(id_i, title, status)
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
        for task in self.task.values():
            print(task)

    def edit_task(self, id_i):
        if id_i in self.task:
            new_task = input("new task: ")
            new_status = input("new status: ")
            self.task[id_i].title = new_task or self.task[id_i].name
            self.task[id_i].status = new_status or self.task[id_i].status
            print("Edited!")
        else:
            print("not found!")
            
    def search_title(self,title):
        flag=False
        for task in self.task.values():
            if task.title == title:
                print(f"Yes It's found:{task}")
                flag = True
        if not flag:
            print("Not Found!,Please Try Again Later.")
        
    def search_id(self,id_i):
        flag=False
        if id_i in self.task:
            print(f"Found:{self.task[id_i]} ")
            flag = True
        else:
            print("Not Found!")

    def search_done(self):
        for task in self.task.values():
            if task.status == "Completed":
                print(task)
        
    def search_undone(self):
        for task in self.task.values():
            if task.status == "InCompleted":
                print(task)

if __name__ == "__main__":
    t1=Todolost_manager()
    print(t1.task)
    task1 = t1.create_task("1", "Exercise", "Completed") 
    task2 = t1.create_task("2", "Shopping", "InCompleted")
    task3 = t1.create_task("3", "Homework", "Completed")
    task4 = t1.create_task("4", "Exercise", "Completed")
    task5 = t1.create_task("5", "Programing", "InCompleted")
    task1 = t1.create_task("1", "Exercise", "Completed") 
    #print(task1)
    t1.add_task(task1)
    t1.add_task(task2)
    t1.add_task(task3)
    t1.add_task(task4)
    t1.add_task(task5)
    #t1.display_task()
    #t1.edit_task("2")
    #t1.display_task()
    #t1.search_title("shopping")
    #t1.search_id("1")
    #t1.search_done()
    t1.search_undone()
