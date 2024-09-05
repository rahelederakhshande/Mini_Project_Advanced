from Todolist import *
from C_Task import *
def main():
    list1=Todolost_manager()
    #list2=Task()
    while True:
        cmd= input("add,remove,display,edit,mark_done,mark_undone,search_name,search_id,search_done,search_undone,mark_done,mark_undone,exit: ")
        if cmd == "add":
            id_i=input("Insert ID For Your Task: ")
            name= input("Insert Name Of Task: ")
            task1 = Task(id_i, name)
            list1.add_task(task1)

        elif cmd == "remove":
            id_i=input("Insert ID For Remove: ")
            list1.remove_task(id_i)

        elif cmd == "display":
            list1.display_task()
        
        elif cmd == "edit":
            id_i=input("Insert ID For Edit: ")
            list1.edit_task(id_i)
        
        elif cmd == "mark_done":
            id_i= input("Insert ID: ")
            if id_i in list1.task:
                list1.task[id_i].done()
                print(f"Task {id_i} marked as done.")

        elif cmd == "mark_undone":
            id_i= input("Insert ID: ")
            if id_i in list1.task:
                list1.task[id_i].undone()
                print(f"Task {id_i} marked as undone.")
                
            

        elif cmd == "search_name":
            name= input("Insert name to find in Task: ")
            list1.search_name(name)
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