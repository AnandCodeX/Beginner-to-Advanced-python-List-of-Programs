#wamdoopp for class employee:
#iv:eid,name,esalary 
#pi:for eid,name,esalary
#im:show(),cal_bonus()
#sv:ecount
#sm:show_ecount

class employee:
    def __init__(self,eid,ename,esalary):
        self.eid=eid
        self.ename=ename
        self.esalary=esalary
        employee.ecount=employee.ecount +1
    
    def show(self):
        print("eid = ",self.eid)
        print("ename =",self.ename)
        print("esalary",self.esalary)
    
    def cal_bonus(self):
        ans=self.esalary*0.10
        print("bonus is =",round(ans,2))
    
    @staticmethod
    def show_ecount():
        print("employee count =",employee.ecount)

list_of_emp =[]
while True:
    op=int(input("1-ADD 2-VIEW 3-DELETE 4 EXIT"))
    if op==1:
        eid=int(input("enter emp id"))
        ename=input("enter name")
        esalary=float(input("enter salary"))
        e=employee(eid,ename,esalary)
        list_of_emp.append(e)
    elif op==2:
        employee.show_ecount()
        for e in list_of_emp:
            print("*"*40)
            e.show()
    elif op==3:
        eid=int(input("enter employee id"))
        for e in list_of_emp:
            if e.eid==eid:
                list_of_emp.remove(e)
                employee.ecount=employee.ecount-1
    elif op==4:
        break
    else:
        print("Invalid option")

        
