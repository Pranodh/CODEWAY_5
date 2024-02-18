from datetime import datetime,timedelta
class Todolist:
    def __init__(self):
        self.task = {}
    def add_work (self,work,due_date):
        self.task[work] = due_date
        print(f"{work} added to todolist")
    def mark_as_complete (self,work):
        
            del self.task[work] 
            print(f"{work} mark as completed")
        

    def remove_work (self,work):
        del self.task[work]
        print(f"{work} removed")
    def due_date_duration (self):
        if (len(self.task)>0):
            for w,d in (self.task).items():
                if (datetime.strptime(d,"%d/%m/%Y")<datetime.now()):
                    print(f"{w} expired")
                else:
                    print(str(w)+" - "+str(datetime.strptime(d,"%d/%m/%Y")-(datetime.now()))+" remaining" )
        else:
            print("No works")
                
            
    def view_work_list (self):
        if (len(self.task)>0):
        
            works_list = list((self.task).items())
        
            for i in works_list:
                print(i)
        else:
            print("No works\n To add click 1")
if __name__ == "__main__":
    todo_list = Todolist()
    while True:
        print("Hi Welcome !")
        print("1.Add work\n2.View Work\n3.Mark as complete\n4.Remove work\n5.work dues\n6.exit\n")
        Task = int(input("Enter your choice 1/2/3/4/5 :"))
        if (Task == 1):
            work = (input("Enter the work: "))
            try:
                due_date=input("Enter due_date (eg:DD/MM/YYYY): ")
                due_date=datetime.strptime(due_date,"%d/%m/%Y")
    
                todo_list.add_work(work,(due_date.strftime("%d/%m/%Y")))
            except ValueError:
                print("Enter Valid Date") 
        elif(Task == 2):
            todo_list.view_work_list()
        elif(Task == 3):
            work=input("Enter the work :")
            if (work in todo_list.task):
                todo_list.mark_as_complete(work)
            else:
                print("Enter valid work")
        elif(Task == 4):
            work=input("Enter the work to be removed :")
            work=input("Enter the work :")
            if (work in todo_list.task):
                todo_list.remove_work(work)
            else:
                print("Enter valid work")
        elif (Task == 5):
            todo_list.due_date_duration()
        elif(Task == 6):
            break
        else:
            print("Enter valid Input")