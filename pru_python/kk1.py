
import sqlite3 as sqlite

y=5
#x=20

class C(object):
	def pepe(self):
		print "hola "


class B(C):
	def pepe2(self):
		print "hola2"


class A(B):
	pass

class J(B,C):
	pass

#db1 = sqlite.connect('test.db')
#
#db1_cr1 = db1.cursor()
#
#db1_cr1.execute('select * from zz')
#
#vec  =  db1_cr1.fetchmany()
#print vec, type(vec)
#
#db1_cr1.close()

