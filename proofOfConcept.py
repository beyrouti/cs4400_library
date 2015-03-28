#Proof Of Concept

import pymysql
try:
    from Tkinter import *
except importError:
    from tkinter import *


class Lms:

    def __init__(self, win):

        self.win = win
        self.LoginPage()

        self.top = Toplevel()
        self.top.title("Registration")
        self.Register()
        self.top.withdraw()
        self.top.protocol("WM_DELETE_WINDOW", self.top.withdraw())
        
 

    def Connect(self):
        try:
            self.db = pymysql.connect(host='academic-mysql.cc.gatech.edu',user='cs4400_Group_41',
            db='cs4400_Group_41',passwd='YIBz9hoA')

        except:
            messagebox.showwarning("Internet Connection Error!", "Please check your internet connection!")
            return None
        


    def LoginPage(self):                                    # Creates Login GUI.
        
        l = Label(self.win, text = "Login", bg = "yellow")
        l.grid(column=0, columnspan=5, stick = EW)

        Label(self.win).grid(row=1, column=0)
        
        Label(self.win, text = "Username").grid(row=2, column=0, sticky=E)
        self.e = Entry(self.win, width=30)
        self.e.grid(row=2,column=1,columnspan=2)
        Label(self.win, text = "Password").grid(row=3, column=0, sticky=E)
        self.e1 = Entry(self.win, width=30)
        self.e1.grid(row=3,column=1,columnspan=2)

        Label(self.win).grid(row=4, column=0)

        Button(self.win, text = "Register", command = self.BackToRegister).grid(row=5,column=1,sticky=E)
        Button(self.win, text = "Login", command = self.LoginCheck).grid(row=5,column=2,sticky=EW)
        Button(self.win, text = "Exit", command=self.win.destroy).grid(row=5,column=3,sticky=E)

    def BackToRegister(self):                                   # Helper function to hide Login window and pop up the Register window.
        self.win.withdraw()
        self.top.deiconify()

    def Register(self):

        l1 = Label(self.top, text = "New User Registration", bg = "yellow")
        l1.grid(column=0, columnspan=5, stick = EW)

        Label(self.top).grid(row=1, column=0)
        

        Label(self.top, text = "Username").grid(row=2, column=0, sticky=W)
        self.e3 = Entry(self.top, width=30)
        self.e3.grid(row=2,column=1,columnspan=2)
        Label(self.top, text = "Password").grid(row=3, column=0, sticky=W)
        self.e4 = Entry(self.top, width=30)
        self.e4.grid(row=3,column=1,columnspan=2)
        Label(self.top, text = "Confirm Password").grid(row=4, column=0, sticky=W)
        self.e5 = Entry(self.top, width=30)
        self.e5.grid(row=4,column=1,columnspan=2)
        Label(self.top, text = "").grid(row=5)

        Button(self.top, text = "Cancel", command = self.BackToLogin).grid(row=6,column=2,sticky=EW)
        Button(self.top, text = "Register", command = self.RegisterNew).grid(row=6,column=4)


    def BackToLogin(self):                                      # Helper function to hide Register window and pop up the Login window.
        self.top.withdraw()
        self.win.deiconify()

    def RegisterNew(self):                                      
        self.Connect()
        username = self.e3.get()
        password = self.e4.get()
        password2 = self.e5.get()

    

        if username == "":                                                                                               # Username entry must not be left blank.
            messagebox.showwarning("Username Error!", "Please enter a username!")
            return


        if password == "":                                                                                               # Password entry must not be left blank.
            messagebox.showwarning("Check password!", "Please enter a password!")
            return

        if password2 == "":                                                                                             # Password must be confirmed.
            messagebox.showwarning("Check password!", "Please confirm password!")
            return

        if password != password2:                                                                                       # Password and confirm password must match.
            messagebox.showwarning("Check password!", "Your password does not match your confirmation password!")
            return


        cursor = self.db.cursor()
        user_sql = "SELECT * FROM User WHERE Username=%s"
        counter = cursor.execute(user_sql, (username,))

        if counter == 1:
            messagebox.showwarning("Username Error!", "Username already exists! Please pick another username.")         # Username must not already exist in database.
            cursor.close()
            self.db.close()
            return

        
                                                                                                    # If LastName entry is not left blank, a last name will be inserted.
        cursor = self.db.cursor()
        sql = "INSERT INTO User (Username, Password) VALUES (%s, %s)"                      # Modelled after DMSI course notes-- "Database Connectivity: SQL Databases".
        cursor.execute( sql, ( username, password) )
        cursor.close()
        self.db.commit()   
        self.db.close()
        messagebox.showwarning("Congratulations!", "Successful Registration!")                                      # Successful Registration if you got this far! 
        self.BackToLogin()

    def LoginCheck(self):                                           # Method that checks to see if username/password combination already exists in database. If so, user is successfully "logged in".
        self.Connect()
        username = self.e.get()
        password = self.e1.get()
        
        cursor = self.db.cursor()
        user_sql = "SELECT * FROM ReservationUser WHERE Username=%s AND Password=%s"
        user_counter = cursor.execute(user_sql, (username,password))


        if user_counter == 0:
            messagebox.showwarning("Username/Password Combination Error!", "Your username/password combination is incorrect!")
            cursor.close()
            self.db.close()
            return
        
        messagebox.showwarning("Success!", "Login successful!")
        self.username = self.e.get()
        self.Homepage()
        self.win.withdraw()




win = Tk()
app = Lms(win)
win.mainloop()






    
