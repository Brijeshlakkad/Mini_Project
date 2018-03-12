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

def add_question(testid,que,a1,a2,a3,a4,ans):
	global cursor,conn
	connect_to_database()
	testid=int(testid)
	sql="Insert into Questions(Question,A1,A2,A3,A4,TestID,Ans) values('%s','%s','%s','%s','%s','%s','%s')"%(que,a1,a2,a3,a4,testid,ans)
	try:
		cursor.execute(sql)
		conn.commit()
		testid=int(testid)
		sql2="Select Total_num from Tests Where ID='%s'"%(testid)
		try:
			cursor.execute(sql2)
			results = cursor.fetchone()
			num=results['Total_num']
			n=int(num)
			n+=1
			sql3="Update Tests SET Total_num='%s' where ID='%s'"%(n,testid)
			try:
				cursor.execute(sql3)
				conn.commit()
				print("1")
			except:
				conn.rollback()
				print("-1")
		except:
			conn.rollback()
			print("-1")
	except:
		conn.rollback()
		print("-1")
	conn.close()

def update_question(queid,que,a1,a2,a3,a4,ans):
	global cursor,conn
	connect_to_database()
	sql="Update Questions SET Question='%s',A1='%s',A2='%s',A3='%s',A4='%s',Ans='%s' where ID='%s'"%(que,a1,a2,a3,a4,ans,queid)
	try:
		cursor.execute(sql)
		conn.commit()
		print("1")
	except:
		conn.rollback()
		print("-1")
	conn.close()


def show_questions(testid):
	global cursor,conn
	connect_to_database()
	sql="Select * FROM Questions where TestID='%s'"%(testid)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			divid=row['ID']
			time=row["Time"]
			datetime=time.strftime('%H : %M')
			que=row['Question']
			print("""<div id="%s" class='style_prevu_kit que_div' style="padding:10px;"><div class="row"><form action="edit_question.php" method="post" ><input type="hidden" name="que_id" value="%s" /><input class="btn btn-link" type="submit" value="%s" /></form></div><div class="row"><div class="col-md-offset-5 col-md-5 col-md-offset-2"> <span class="glyphicon glyphicon-time"></span> Posted on %s</div></div></div><hr/><hr/>"""%(divid,divid,que,time))
	except:
		conn.rollback()
		print("-1")
	conn.close()

def remove_questions_of_test(testid):
	global cursor,conn
	connect_to_database()
	sql="Delete from Questions where TestID='%s'"%(testid)
	try:
		cursor.execute(sql)
		conn.commit()
		print("1")
	except:
		conn.rollback()
		print("-1")
	conn.close()
	
def total_que_num(testid):
	global cursor,conn
	connect_to_database()
	sql="Select Total_num From Tests where ID='%s'"%(testid)
	try:
		cursor.execute(sql)
		results = cursor.fetchone()
		num=results['Total_num']
		print(num)
	except:
		conn.rollback()
		print("-1")
	conn.close()