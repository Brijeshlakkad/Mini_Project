#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import cgi, cgitb 
import sys
import os
import MySQLdb

def connect_to_database():
	global conn,cursor
	conn = MySQLdb.connect (host = "localhost",user = "root",passwd = "",db = "mini_project")
	cursor = conn.cursor ()
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)

def reload_history(c_id1):
	global cursor,conn
	connect_to_database()
	sql="SELECT * FROM History where UserID='%s' ORDER BY Time DESC"%(c_id1)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			divid=row['ID']
			time=row["Time"]
			datetime=time.strftime('%H : %M')
			field=row['Field']
			fdiv="You have updated <strong> %s</strong> at %s"%(field,datetime)
			print("""<div id="%s"  class="alert alert-info alert-dismissable fade in" ><a href="#" onclick='delete_hist("%s")' class="close" data-dismiss="alert" aria-label="close">&times;</a> %s </div><br/>"""%(divid,divid,fdiv))
	except:
		conn.rollback()
		print("Try again !")
	conn.close()

def delete_history(c_id1):
	global cursor,conn
	connect_to_database()
	sql="DELETE FROM History where ID='%s'"%(c_id1)
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	conn.close()

def delete_all_history(c_id1):
	global cursor,conn
	connect_to_database()
	sql="DELETE FROM History where UserID='%s'"%(c_id1)
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	conn.close()
	
def history_total_count(c_id1):
	global cursor,conn
	connect_to_database()
	sql="SELECT * FROM History where UserID='%s'"%(c_id1)
	try:
		cursor.execute(sql)
		results=cursor.rowcount
		rownum="%s"%results
		print(rownum)
		conn.commit()
	except:
		conn.rollback()
		print("0")
	conn.close()