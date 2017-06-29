#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('test.db')
print "opened database successfully"
def insert():
	conn.execute("INSERT INTO projects(username,pswd,name,begin_date,end_date) VALUES ('abc','123','sita','16 june 2017','17 june 2017' )");
	conn.execute("INSERT INTO projects(username,pswd,name,begin_date,end_date) VALUES ('pqr','456','gita','15 june 2017','16 june 2017' )");
	conn.execute("INSERT INTO projects(username,pswd,name,begin_date,end_date) VALUES ('mno','789','mita','16 may 2017','17 may 2017' )")
	conn.execute("INSERT INTO projects(username,pswd,name,begin_date,end_date) VALUES ('xyz','012','nita','15 may 2017','17 may 2017' )")
	conn.execute("INSERT INTO projects(username,pswd,name,begin_date,end_date) VALUES ('def','235','kita','17 june 2017','18 june 2017' )")
	conn.commit()
	print "records created successfully"
def select():
	cursor = conn.execute("SELECT username,pswd,name from projects")
	for row in cursor:
		print "Username:", row[0]
		print "password:", row[1]
		print "name:", row[2]
	print "operation done succesfully","\n"
def update():
	name = 'hello'
	username = 'mno'
	conn.execute('''UPDATE PROJECTS set name = ? where username = ?''', (name, username))
	conn.commit()
	cursor = conn.execute("SELECT username,pswd,name from projects")
	for row in cursor:
		print "Username:", row[0]
		print "password:", row[1]
		print "name:", row[2]
	print "operation done succesfully","\n"
def delete():
	username = 'pqr'
	conn.execute('''DELETE from projects where username = ?''',[username])
	conn.commit()
	cursor = conn.execute("SELECT username,pswd,name from projects")
	for row in cursor:
		print "Username:", row[0]
		print "password:", row[1]
		print "name:", row[2]
	print "operation done succesfully","\n"