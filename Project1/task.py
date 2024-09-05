from datetime import *
class Task:
    state= None
    def __init__(self,id_i,title,status):
        self.id_i = id_i
        self.title = title
        self.status = status
        self.date_of_finishing = None

    def __str__(self):
        return f"ID:{self.id_i},Title:{self.title},Status:{self.status}"

    def done(self,id_i):
        try:
            if self.id_i == id_i:
                self.status = "Completed"
                self.date_of_finishing = datetime.now()
                Task.state = True
                print(f"This Task is Completed at:{self.date_of_finishing}")
            else:
                print("Not Available!")
        except TypeError:
            print("please try again later!")
            
    def undone(self,id_i):
        if self.id_i == id_i:
            self.status = "InCompleted"
            Task.state= False
        else:
            print("Not Available!")
            
        


if __name__ == "__main__":
    task1=Task("1","homework","")
    task1.undone()
    task2=Task("2","Final_Project","")
    task2.done()
    print(task1)
    print(task2)
