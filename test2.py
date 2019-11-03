import sqlite3
from datetime import datetime



def renew_vregistration(cursor, conn):

    vregno = input('Please enter the vehicles registration number')
    today = datetime.date(datetime.now()) #datetime error here

    exp = None
    while exp == None:
        cursor.execute('select r.expiry from registrations r where r.regno = ?;', (vregno,))
        exp = cursor.fetchone()
        if exp == None:
            vregno = input('Please enter a valid registration number')
    
    exp = exp[0]
    currexp = exp.split('-')
    ndate = today
    ndate = ndate.replace(year = int(currexp[0]), month = int(currexp[1]), day = int(currexp[2]))
    
    if today >= ndate:

        ndate = today
        ndate = ndate.replace(year = today.year + 1)
        
    else:
        
        ndate = ndate.replace(year = ndate.year + 1)
    
    ndate = ndate.strftime('%Y-%m-%d')

    cursor.execute('update registrations set expiry = ? where regno = ?;', (ndate, vregno,))
    conn.commit()

dbpath = "./a2.db"
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursor.execute(' PRAGMA foreign_keys=ON; ')
print('Register renewreg test')
renew_vregistration(cursor, conn)
print('ALL DONE!!!')
