#Proof Of Concept

import pymysql
import Tkinter

class Lms:

    def __init__(self, top):
        self.top = top
        unButton = Tkinter.Button(top, text= "push me", command = self.helloWorld)
        unButton.pack()
        
 

    def helloWorld(self):
        db = pymysql.connect(host='academic-mysql.cc.gatech.edu',user='cs4400_Group_41',
        db='cs4400_Group_41',passwd='YIBz9hoA')
        cursor = db.cursor()
        sql = 'SELECT Username FROM User'
        result = cursor.execute(sql)
        usernames = cursor.fetchall()
        print(usernames)

    # result carries the value of the number of tuples that will be affected by the SQL statement



top = Tkinter.Tk()
app = Lms(top)
top.mainloop()




    
