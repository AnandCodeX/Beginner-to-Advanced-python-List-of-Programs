class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def show(self):
        print("id=",self.id)
        print("name=",self.name)

class teacher(person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def show(self):
        super().show()
        print("salary =",self.salary)

class hod(teacher):
    def __init__(self,id,name,salary,dept):
        super().__init__(id,name,salary)
        self.dept=dept
    def show(self):
        super().show()
        print("dept =",self.dept)

h=hod(10,'amit',3000,"comp")
h.show
        