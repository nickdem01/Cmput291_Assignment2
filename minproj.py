import sqlite3
import random
from date import datetime

def register_birth(login):

	bregno = random.randint(100000,999999)
	
	row = None
	cursor.execute('select * from births b where b.regno = ?;', (bregno,))
	row = cursor.fetchone()
	
	if row != None:
		
		while row != None:

	                bregno = random.randint(100000,999999)

        		row = None
        		cursor.execute('select * from births b where b.regno = ?;', (bregno,))
        		row = cursor.fetchone()

	
	bfname = input('What is the first name of the baby')
	blname = input('What is the last name of the baby')

	bregdate = datetime.date(datetime.now())

	cursor.execute('select u.city from users u where u.uid = ?;', (login,))
	bregplace = cursor.fetchone()

	nbplace = input('What is the birth place')
	
	bgender = 'l'

	while bgender != 'M' or bgender != 'F':

		bgender = input('What is the gender of the child (M or F)?')
		bgender = bgender.upper()	

		
	p1Fname = input('What is the first name the Mother')
	p1Lname = input('What is the last name of the Mother')
	
	#check if parent 1 exists
	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p1Fname,), (p1Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Mother info missing please enter the missing data')

		paFname = input('Please enter the first name of Mother')
		paLname = input('Please enter the last name of Mother')
		pabDate	= input('Please enter the birthdate of Mother')
		pabPlace = input('Please enter the birthplace of Mother')
		paAddress = input('Please enter the address of Mother')
		paPhone = input('Please enter the phone number of Mother')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	p2Fname = input('What is the first name of the Father')
	p2Lname = input('What is the last name of the Father')
	
	#check existence of Father
        cursor.execute('select * from persons p where p.fname = ? and p.lname = ?',(p2Fname,), (p2Lname,))
        row = cursor.fetchone()

        if row  == None:

                print('Father info missing please enter the missing data')

                paFname = input('Please enter the first name of Father')
                paLname = input('Please enter the last name of Father')
                pabDate = input('Please enter the birthdate of Father')
                pabPlace = input('Please enter the birthplace of Father')
                paAddress = input('Please enter the address of Father')
                paPhone = input('Please enter the phone number of Father')

                cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
                conn.commit()

	cursor.execute('insert into births values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', (bregno, bfname, blname, bregdate, bregplace, bgender, p1Fname, p1Lname, p2Fname, p2Lname)) 
	conn.commit()

	#create the persons entry
	
	nbdate = input('Please enter the birthdate of the baby')
	
	cursor.execute('select p.address from persons p where p.fname = ? and p.lname = ?;', (p1Fname, p1Lname))
	baddress = cursor.fetchone()


	cursor.execute('select p.phone from persons p where p.fname = ? and p.lname = ?;', (p1Fname, p1Lname))
	bphone = cursor.fetchone()

	cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (bfname, blname, nbdate, nbplace, baddress, bphone))
	conn.commit


def registerMarriage():
	
	p1Fname = input('Please enter the first name of Partner 1')
	p1Lname = input('Please enter the last name of Partner 1')
	p2Fname = input('Please enter the first name of Partner 2')
	p2Lname = input('Please enter the last name of Partner 2')
	

	mregdate = datetime.date(datetime.now())

	mregno = random.randint(100000,999999)
	
	row = None
	cursor.execute('select * from marriages m where m.regno = ?;', (mregno,))
	row = cursor.fetchone()
	
	if row != None:
		
		while row != None:

	                mregno = random.randint(100000,999999)

        		row = None
        		cursor.execute('select * from marriages m where m.regno = ?;', (mregno,))
        		row = cursor.fetchone()

	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p1Fname,), (p1Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Partner 1 info missing please enter the missing data')

		paFname = input('Please enter the first name of Partner 1')
		paLname = input('Please enter the last name of Partner 1')
		pabDate	= input('Please enter the birthdate of Partner 1')
		pabPlace = input('Please enter the birthplace of Partner 1')
		paAddress = input('Please enter the address of Partner 1')
		paPhone = input('Please enter the phone number of Partner 1')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	row = None 
	cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p2Fname,), (p2Lname,))
	row = cursor.fetchone()
	
	if row  == None:
		
		print('Partner 2 info missing please enter the missing data')

		paFname = input('Please enter the first name of Partner 2')
		paLname = input('Please enter the last name of Partner 2')
		pabDate	= input('Please enter the birthdate of Partner 2')
		pabPlace = input('Please enter the birthplace of Partner 2')
		paAddress = input('Please enter the address of Partner 2')
		paPhone = input('Please enter the phone number of Partner 2')
		
		cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (paFname, paLname, pabDate, pabPlace, paAddress, paPhone))
		conn.commit()

	cursor.execute('inset into marriages values (?, ?, ?, ?, ?, ?, ?);', (mregno, mregdate, mregplace, p1Fname, p1Lname, p2Fname, p2Lname))
	conn.commit()
			
main():

	
	#dbpath code needs to be edited to accomadate command line arg database code will not function on your computer as it is now
	dbpath = "./a2.db"
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	cursor.execute(' PRAGMA foreign_keys=ON; ')
	t = 'Goldi'
	cursor.execute('select * from persons p where p.fname = ?;', (t,))
	row = cursor.fetchone()
	
	

main()
