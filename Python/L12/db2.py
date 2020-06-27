#wapp to connect and disconnect from Oracle Db

import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected ")
	rno = int(input("enter rno "))
	name = input("enter name ")
	args=(rno, name)
	cursor = con.cursor()
	sql = "insert into student_thane_jan20 values('%d', '%s')"
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount, " records inserted ")
except cx_Oracle.DatebaseError as e:
	print("issue", e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")