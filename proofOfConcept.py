#Proof Of Concept

import pymysql
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class Lms:

    def __init__(self, top):
        self.top = top
        unButton = Button(top, text= "push me", command = self.helloWorld)
        unButton.pack()

        self.sv1 = StringVar()
        self.userentry = Entry(self.top, textvariable=self.sv1,width=30)
        self.userentry.pack()

        self.sv2 = StringVar()
        self.passentry = Entry(self.top, textvariable=self.sv2,width=30)
        self.passentry.pack()


    def helloWorld(self):
        db = pymysql.connect(host='academic-mysql.cc.gatech.edu',user='cs4400_Group_41',
        db='cs4400_Group_41',passwd='YIBz9hoA')
        cursor = db.cursor()
        sql = 'SELECT Username FROM User'
        result = cursor.execute(sql)
        usernames = cursor.fetchall()
        print(usernames)

        inputusername = self.sv1.get()
        inputpassword = self.sv2.get()
        print(inputusername)
        print(inputpassword)

    # result carries the value of the number of tuples that will be affected by the SQL statement



top = Tk()
app = Lms(top)
top.mainloop()




    
