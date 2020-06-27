''' wapp for foll:-
class Employee with IV:- eid, ename, epds(per day salary)
class Attendance with IV:- nodp(no of days present)

e = Employee(10, "Amit", 500)
a = Attendance(25)
sal = e*a
'''

class Employee:
	def __init__(self, eid, ename, epds):
		self.eid = eid
		self.ename = ename
		self.epds = epds
	def __mul__(self, other):
		res = self.epds * other.nodp	
		return res

class Attendance:
	def __init__(self, nodp):
		self.nodp = nodp

e = Employee(10, "Amit", 500)
a = Attendance(25)

sal = e * a;	print(sal)