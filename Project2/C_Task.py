from datetime import *
class Task:
    def __init__(self,id_i,name, state=False,date_of_finishing = None):
        self.id_i = id_i
        self.name= name
        self.state = state
        self.date_of_finishing = date_of_finishing

        
    def __str__(self):
        status = "Completed" if self.state else "InCompleted"
        return f"ID: {self.id_i}, Name: {self.name}, Status: {status}, Date of Finishing: {self.date_of_finishing}"

    def done(self):
        self.state = True
        self.date_of_finishing=datetime.now()

    def undone(self):
        self.state=False
        self.date_of_finishing=None
    
        


if __name__ == "__main__":
    task1=Task("1","homework")
    task1.undone()
    task2=Task("2","Final_Project")
    task2.done()
    print(task1)
    print(task2)
