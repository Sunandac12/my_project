#!/usr/bin/python
import sqlite3
from connect import create_connection
from crud import insert
from crud import select
from crud import update
from crud import delete
def se():
	while(1):
		print "your options are:"
		print "1) insert"
		print "2) select"
		print "3) update"
		print "4) delete"
		print "5) quit"
		option = input("choose your option:")
		if option == 1:
			insert()
		elif option == 2:
			select()
		elif option == 3:
			update()
		elif option == 4:
			delete()
		else:
			quit()
def quit():
	print quit

se()