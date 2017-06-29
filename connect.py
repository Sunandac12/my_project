#!/usr/bin/python
import sqlite3
def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		conn = create_connection(database)
		return conn
	except Error as e:
		print(e)
	return None

def create_table(conn, create_table_sql):
	try:
		c= conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def main():
	database = '/home/sunanda/Documents/database/test.db'
	sql_create_projects_table =" ""CREATE TABLE IF NOT EXISTS projects (username text NOT NULL, pswd text NOT NULL, name text NOT NULL, begin_date text,end_date text ); """
	if conn is not None:
		create_table(conn, sql_create_projects_table)
	else:
		print "Error"

if __name__ == '__main__':
	main()