#wapp to connect and disconnect from Oracle Db

import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected ")
	cursor = con.cursor()
	sql = "select rno, name from student_thane_jan20"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("rno=", d[0], "name=", d[1])
	
except cx_Oracle.DatebaseError as e:
	print("issue", e)
	
finally:
	if con is not None:
		con.close()
		print("disconnected")