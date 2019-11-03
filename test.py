import sqlite3
from datetime import datetime
import random

def registerMarriage(cursor, conn):

    p1Fname = input('Please enter the first name of Partner 1')
    p1Lname = input('Please enter the last name of Partner 1')
    p2Fname = input('Please enter the first name of Partner 2')
    p2Lname = input('Please enter the last name of Partner 2')

    mregdate = datetime.date(datetime.now()) #datetime error here
    mregdate = mregdate.strftime('%Y-%m-%d')

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
    cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p1Fname, p1Lname,))
    row = cursor.fetchone()

    if row  == None:

        print('Partner 1 info missing please enter the missing data')

        pabDate	= input('Please enter the birthdate of Partner 1')
        pabPlace = input('Please enter the birthplace of Partner 1')
        paAddress = input('Please enter the address of Partner 1')
        paPhone = input('Please enter the phone number of Partner 1')

        cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (p1Fname, p1Lname, pabDate, pabPlace, paAddress, paPhone))
        conn.commit()

    row = None
    cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;',(p2Fname, p2Lname,))
    row = cursor.fetchone()

    if row  == None:

        print('Partner 2 info missing please enter the missing data')

        pabDate	= input('Please enter the birthdate of Partner 2')
        pabPlace = input('Please enter the birthplace of Partner 2')
        paAddress = input('Please enter the address of Partner 2')
        paPhone = input('Please enter the phone number of Partner 2')

        cursor.execute('insert into persons values (?, ?, ?, ?, ?, ?);', (p2Fname, p2Lname, pabDate, pabPlace, paAddress, paPhone))
        conn.commit()

    mregplace = input('Please enter the registration place')
    cursor.execute('insert into marriages values (?, ?, ?, ?, ?, ?, ?);', (mregno, mregdate, mregplace, p1Fname, p1Lname, p2Fname, p2Lname)) #mregplace is an undefined variable
    conn.commit()


	
	#dbpath code needs to be edited to accomadate command line arg database code will not function on your computer as it is now
dbpath = "./a2.db"
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursor.execute(' PRAGMA foreign_keys=ON; ')
t = 'Gold'
v = 'Fox'
cursor.execute('select * from persons p where p.fname = ? and p.lname = ?;', (t, v))
row = cursor.fetchone()
print(row)
print('Register marriage test')
registerMarriage(cursor, conn)
print('ALL DONE!!!')
	
