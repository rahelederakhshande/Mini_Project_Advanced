from Todolist import *
from task import *
def main():
    list1=Todolost_manager()
    #list2=Task(id_i,title,status)
    while True:
        cmd= input("add,remove,display,edit,mark_done,mark_undone,search_title,search_id,search_done,search_undone,mark_done,mark_undone,exit: ")
        if cmd == "add":
            id_i=input("Insert ID For Your Task: ")
            title= input("Insert Title Of Task: ")
            status=input("Insert Status: ")
            task=list1.create_task(id_i,title,status)
            list1.add_task(task)

        elif cmd == "remove":
            id_i=input("Insert ID For Remove: ")
            list1.remove_task(id_i)

        elif cmd == "display":
            list1.display_task()
        
        elif cmd == "edit":
            id_i=input("Insert ID For Edit: ")
            list1.edit_task(id_i)
        
        elif cmd == "mark_done":
            try:
                id_i=input("Insert ID of Task To mark as DONE: ")
                #list2.done(id_i)
                Task.done(id_i)
            except TypeError:
                print("Try again")
            
        
        elif cmd == "mark_undone":
            id_i=input("Insert ID of Task To mark as UNDONE: ")
            Task.undone(id_i)

        elif cmd == "search_title":
            title= input("Insert Title to find in Task: ")
            list1.search_title(title)
        elif cmd == "search_id":
            id_i=input("Inser Id FOr Search: ")
            list1.search_id(id_i)
        elif cmd == "search_done":
            list1.search_done()
        elif cmd == "search_undone":
            list1.search_undone()
        
        
        elif cmd == "exit":
            break
        elif cmd == "":
            continue
        else:
            print(f"{cmd}: NOT FOUND!")

        


if __name__ == "__main__":
    main()