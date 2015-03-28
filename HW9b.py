#HW #9b
#CS 2316
#Vishnu Premsankar
#p.vishnu@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials


from tkinter import *
import urllib.request
import pymysql
from tkinter import messagebox
import string


class Reservation:

    def __init__(self,login,register,homepage,available,statistics):
        self.login = login
        self.register = register
        self.homepage = homepage
        self.available = available
        self.statistics = statistics
        
        self.LoginPage(self.login)
        
        self.Register(self.register)
        self.register.withdraw()
        
        self.homepage.withdraw()

        self.available.withdraw()

        self.statistics.withdraw()
        

    def LoginPage(self,login):
        url = 'http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif'
        request = urllib.request.urlopen(url)
        picture = request.read()

        import base64
        b64_data = base64.encodebytes(picture)
        self.photo = PhotoImage(data=b64_data)

        Label(self.login, image=self.photo).grid(row=0,column=1, sticky=EW)
        Label(self.login, text='Username').grid(row=1,column=0, sticky=E)
        Label(self.login, text='Password').grid(row=2,column=0, sticky=E)

        self.sv1 = StringVar()
        self.e1 = Entry(self.login, textvariable=self.sv1, width=30)
        self.e1.grid(row=1, column=1)

        self.sv2 = StringVar()
        self.e2 = Entry(self.login, textvariable=self.sv2, width=30)
        self.e2.grid(row=2, column=1)

        self.b1 = Button(self.login, text='Register',command=self.SwitchtoRegister)
        self.b1.grid(row=3,column=1,sticky=E)

        self.b2 = Button(self.login, text='Login',command=self.LoginCheck)
        self.b2.grid(row=3,column=2,sticky=E)

        self.b3 = Button(self.login, text='Exit',command=self.CloseLogin)
        self.b3.grid(row=3,column=3,sticky=E)

    def SwitchtoRegister(self):
        self.login.withdraw()
        self.register.deiconify()
        
    def LoginCheck(self):
        db = self.Connect()
        cursor = db.cursor()

        self.username = self.sv1.get()
        password = self.sv2.get()

        sql = "SELECT* FROM ReservationUser WHERE Username = %s"
        result = cursor.execute(sql, (self.username,))
        
        if result != 1:
            messagebox.showwarning('Error!', 'Unrecognizable username/password Combination!')
            return

        sql = "SELECT * FROM ReservationUser WHERE Username = %s AND Password = %s"
        result = cursor.execute(sql, (self.username, password))

        if result == 1:
            messagebox.showwarning('Succses!', 'You have successfully Logged in!')
            self.CloseLogin2()
        else:
            messagebox.showwarning('Error!', 'Unrecognizable username/password Combination!')
            return

        cursor.close()
        db.commit()
        db.close()

    def CloseLogin(self):
        self.register.destroy()
        self.login.destroy()


    def CloseLogin2(self):
        self.register.withdraw()
        self.login.withdraw()
        self.Homepage()
        self.homepage.deiconify()
        
    def Register(self,register):
        url = 'http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif'
        request = urllib.request.urlopen(url)
        picture = request.read()

        import base64
        b64_data = base64.encodebytes(picture)
        self.photo2 = PhotoImage(data=b64_data)

        Label(self.register, image=self.photo2).grid(row=0,column=1, sticky=EW)
        Label(self.register, text='Last Name').grid(row=1,column=0, sticky=W)
        Label(self.register, text='Username').grid(row=2,column=0, sticky=W)
        Label(self.register, text='Password').grid(row=3,column=0, sticky=W)
        Label(self.register, text='Confirm Password').grid(row=4,column=0, sticky=W)

        self.svv1 = StringVar()
        self.ee1 = Entry(self.register, textvariable=self.svv1, width=30)
        self.ee1.grid(row=1,column=1)

        self.svv2 = StringVar()
        self.ee2 = Entry(self.register, textvariable=self.svv2, width=30)
        self.ee2.grid(row=2,column=1)

        self.svv3 = StringVar()
        self.ee3 = Entry(self.register, textvariable=self.svv3, width=30)
        self.ee3.grid(row=3,column=1)

        self.svv4 = StringVar()
        self.ee4 = Entry(self.register, textvariable=self.svv4, width=30)
        self.ee4.grid(row=4,column=1)

        Label(self.register, text=' ').grid(row=5,column=2)

        self.bb1 = Button(self.register, text='Cancel',command=self.BacktoLogin)
        self.bb1.grid(row=6,column=2)

        self.bb2 = Button(self.register, text='Register',command=self.RegisterNew)
        self.bb2.grid(row=6, column=3)


    def BacktoLogin(self):
        self.register.withdraw()
        self.login.deiconify()

    def RegisterNew(self):
        lastname = self.svv1.get()
        username = self.svv2.get()
        password = self.svv3.get()
        confirmpassword = self.svv4.get()

        if password != confirmpassword:
            messagebox.showwarning('Error!', 'Password entries do not match!')
            return
        if password == "":
            messagebox.showwarning('Error!', 'Make sure to enter the password twice!')
            return
        if confirmpassword == '':
            messagebox.showwarning('Error!', 'Make sure to enter the password twice!')
            return
        if len(username) <= 15:
            pass
        else:
            messagebox.showwarning('Error!', 'Make sure the username has less than or equal to 15 characters!')
            return
        
        num = 'no'
        capitalletter = 'no'
        for item in password:
            if item in string.digits:
                num = 'yes'
            if item in string.ascii_uppercase:
                capitalletter = 'yes'

        if num == 'no':
            messagebox.showwarning('Error!', 'Invalid Password. Make sure to include at least one capital letter and one number!')
            return
        if capitalletter == 'no':
            messagebox.showwarning('Error!', 'Invalid Password. Make sure to include at least one capital letter and one number!')
            return

        db = self.Connect()
        cursor = db.cursor()
        sql = "SELECT* FROM ReservationUser WHERE Username = %s"
        result = cursor.execute(sql, (username,))

        if result == 1:
            messagebox.showwarning('Error!', 'This username already exists!')
            return

        if lastname != '':
            sql = "INSERT INTO ReservationUser(Username,Password,Lastname,NumberOfReservations) VALUES (%s,%s,%s,%s)"
            result2 = cursor.execute(sql, (username,password,lastname,0))
            messagebox.showwarning('Success!','You have been registered!')
            self.BacktoLogin()
        else:
            sql = 'INSERT INTO ReservationUser(Username,Password,NumberOfReservations) VALUES (%s,%s,%s)'
            result2 = cursor.execute(sql, (username, password,0))
            messagebox.showwarning('Success!', 'You have been registered!')
            self.BacktoLogin()

        cursor.close()
        db.commit()
        db.close()

    def Connect(self):
        try:
            db = pymysql.connect(host='academic-mysql.cc.gatech.edu',
                             user='vpremsankar3', db='cs2316db',
                             passwd = 'PxNbR2hz')

            return db

        except:
            messagebox.showwarning('Error!','Check Internet Connection!')


    def Homepage(self):
        Label(self.homepage, text='Welcome To GT Room Reservation System!', relief='raised').grid(row=0,column=1,columnspan=3)
        Label(self.homepage, text=' ').grid(row=1,column=2)
        Label(self.homepage, text='Current Reservations').grid(row=2,column=0,sticky=E)

        self.hpsv1 = StringVar()
        self.hpe1 = Entry(self.homepage, textvariable=self.hpsv1, state='readonly')
        self.hpe1.grid(row=2,column=1,columnspan=4,sticky=EW)

        Label(self.homepage, text=' ').grid(row=3,column=2)
        Label(self.homepage, text=' ').grid(row=4,column=2)

        Label(self.homepage, text='Make New Reservations:').grid(row=5,column=0,sticky=W)
        

        self.dc = IntVar()
        self.daychoices = Frame(self.homepage,bd=2,relief=SUNKEN)
        self.daychoices.grid(row=6,column=0)
        Label(self.daychoices, text='Day Choices').pack()
        self.monday = Radiobutton(self.daychoices,text='Monday',variable=self.dc, value=1)
        self.monday.pack(anchor=W)
        self.tuesday = Radiobutton(self.daychoices,text='Tuesday',variable=self.dc, value=2)
        self.tuesday.pack(anchor=W)
        self.wednesday = Radiobutton(self.daychoices,text='Wednesday',variable=self.dc, value=3)
        self.wednesday.pack(anchor=W)
        self.thursday = Radiobutton(self.daychoices,text='Thursday',variable=self.dc, value=4)
        self.thursday.pack(anchor=W)
        self.friday = Radiobutton(self.daychoices,text='Friday',variable=self.dc, value=5)
        self.friday.pack(anchor=W)

        self.tc = IntVar()
        self.timechoices = Frame(self.homepage, bd=2, relief=SUNKEN)
        self.timechoices.grid(row=6, column=1, sticky=W)
        Label(self.timechoices, text='Time Choices').pack()
        self.morning = Radiobutton(self.timechoices, text='Morning',variable=self.tc, value=1)
        self.morning.pack(anchor=W)
        self.afternoon = Radiobutton(self.timechoices, text='Afternoon',variable=self.tc, value=2)
        self.afternoon.pack(anchor=W)
        self.evening = Radiobutton(self.timechoices, text='Evening',variable=self.tc, value=3)
        self.evening.pack(anchor=W)
        self.night = Radiobutton(self.timechoices, text='Night',variable=self.tc, value=4)
        self.night.pack(anchor=W)

        self.bc = IntVar()
        self.buildingchoices = Frame(self.homepage, bd=2, relief=SUNKEN)
        self.buildingchoices.grid(row=6, column=2, sticky=E)
        Label(self.buildingchoices, text='Building Choices').pack()
        self.culc = Radiobutton(self.buildingchoices, text='CULC', variable=self.bc, value=1)
        self.culc.pack()
        self.klaus = Radiobutton(self.buildingchoices, text='Klaus', variable=self.bc, value=2)
        self.klaus.pack()

        self.fc = IntVar()
        self.floorchoices = Frame(self.homepage, bd=2, relief=SUNKEN)
        self.floorchoices.grid(row=6, column=3, sticky=E)
        Label(self.floorchoices, text='Floor Choices').pack()
        self.floor1 = Radiobutton(self.floorchoices, text='1', variable=self.fc, value=1)
        self.floor1.pack()
        self.floor2 = Radiobutton(self.floorchoices, text='2', variable=self.fc, value=2)
        self.floor2.pack()
        self.floor3 = Radiobutton(self.floorchoices, text='3', variable=self.fc, value=3)
        self.floor3.pack()
        self.floor4 = Radiobutton(self.floorchoices, text='4', variable=self.fc, value=4)
        self.floor4.pack()

        self.rc = IntVar()
        self.roomchoices = Frame(self.homepage, bd=2, relief=SUNKEN)
        self.roomchoices.grid(row=6, column=4, columnspan=2)
        Label(self.roomchoices, text='Room Choices').grid(row=0,column=0,columnspan=2)
        self.r1 = Radiobutton(self.roomchoices, text='1', variable=self.rc, value=1)
        self.r1.grid(row=1,column=0)
        self.r2 = Radiobutton(self.roomchoices, text='2', variable=self.rc, value=2)
        self.r2.grid(row=2,column=0)
        self.r3 = Radiobutton(self.roomchoices, text='3', variable=self.rc, value=3)
        self.r3.grid(row=3,column=0)
        self.r4 = Radiobutton(self.roomchoices, text='4', variable=self.rc, value=4)
        self.r4.grid(row=4,column=0)
        self.r5 = Radiobutton(self.roomchoices, text='5', variable=self.rc, value=5)
        self.r5.grid(row=5,column=0)
        self.r6 = Radiobutton(self.roomchoices, text='6', variable=self.rc, value=6)
        self.r6.grid(row=1,column=1)
        self.r7 = Radiobutton(self.roomchoices, text='7', variable=self.rc, value=7)
        self.r7.grid(row=2,column=1)
        self.r8 = Radiobutton(self.roomchoices, text='8', variable=self.rc, value=8)
        self.r8.grid(row=3,column=1)
        self.r9 = Radiobutton(self.roomchoices, text='9', variable=self.rc, value=9)
        self.r9.grid(row=4,column=1)
        self.r10 = Radiobutton(self.roomchoices, text='10', variable=self.rc, value=10)
        self.r10.grid(row=5,column=1)

        Label(self.homepage, text='                        ').grid(row=7, column=3, sticky=E)
        Label(self.homepage, text='                        ').grid(row=7, column=1)
        Label(self.homepage, text='                           ').grid(row=7, column=4)


        self.hpb1 = Button(self.homepage, text='Cancel All Reservations', command=self.cancelReservation)
        self.hpb1.grid(row=8,column=0,sticky=EW)
        self.hpb2 = Button(self.homepage, text='Check Available Options', command=self.availableReservations)
        self.hpb2.grid(row=8,column=1,columnspan=2,sticky=EW)
        self.hpb3 = Button(self.homepage, text='Stats', command=self.stats)
        self.hpb3.grid(row=8,column=3,sticky=EW)
        self.hpb4 = Button(self.homepage, text='Logout', command=self.HomepageToLogin)
        self.hpb4.grid(row=8,column=4,sticky=EW)


        self.username = self.sv1.get()
        db = self.Connect()
        cursor = db.cursor()
        sql = 'SELECT * FROM RoomReservations WHERE ReservedBy = %s'
        cursor.execute(sql, (self.username,))
        infoList = cursor.fetchall()

        listofmessages = []
        for item in infoList:
            message = 'Room ' + str(item[2]) + ' on ' + item[0] + ' floor ' + str(item[1]) + ' is reserved for ' + item[3] + ' at ' + item[4] + ' hours'
            listofmessages.append(message)

        self.numentries = len(listofmessages)

        if self.numentries == 0:
            self.hpsv1.set('No Reservations')
        elif self.numentries == 1:
            self.hpsv1.set(listofmessages[0])
        elif self.numentries == 2:
            self.hpsv1.set(listofmessages[0])
            self.hpsv2 = StringVar()
            self.hpe2 = Entry(self.homepage, textvariable=self.hpsv2, state='readonly')
            self.hpe2.grid(row=3,column=1,columnspan=4,sticky=EW)
            self.hpsv2.set(listofmessages[1])

        cursor.close()
        db.commit()
        db.close()

    def availableReservations(self):

        if self.dc.get() == 0:
            messagebox.showwarning('Search Failure', 'Please choose a valid option from each category')
            return
        if self.tc.get() == 0:
            messagebox.showwarning('Search Failure', 'Please choose a valid option from each category')
            return
        if self.bc.get() == 0:
            messagebox.showwarning('Search Failure', 'Please choose a valid option from each category')
            return
        if self.fc.get() == 0:
            messagebox.showwarning('Search Failure', 'Please choose a valid option from each category')
            return
        if self.rc.get() == 0:
            messagebox.showwarning('Search Failure', 'Please choose a valid option from each category')
            return

        roomnumber = self.rc.get()
        floornumber = self.fc.get()

        if self.bc.get() == 1:
            building = 'CULC'
        elif self.bc.get() == 2:
            building = 'Klaus'

        if self.tc.get() == 1:
            time = 'Morning'
        elif self.tc.get() == 2:
            time = 'Afternoon'
        elif self.tc.get() == 3:
            time = 'Evening'
        elif self.tc.get() == 4:
            time = 'Night'

        if self.dc.get() == 1:
            day = 'Monday'
        elif self.dc.get() == 2:
            day = 'Tuesday'
        elif self.dc.get() == 3:
            day = 'Wednesday'
        elif self.dc.get() == 4:
            day = 'Thursday'
        elif self.dc.get() == 5:
            day = 'Friday'


        db = self.Connect()
        cursor = db.cursor()
        sql = 'SELECT Time FROM RoomReservations WHERE Building = %s AND Floor = %s AND RoomNo = %s AND Day = %s'

        cursor.execute(sql, (building, floornumber, roomnumber, day))
        exreservations = cursor.fetchall()

        newexres = []
        for item in exreservations:
            for i in item:
                newexres.append(i)

        print(newexres)
            

        morningList = ['08:00','09:00','10:00','11:00']
        afternoonList = ['12:00','13:00','14:00','15:00']
        eveningList = ['16:00','17:00','18:00','19:00']
        nightList = ['20:00','21:00','22:00','23:00']

        availabletimes = 0
        
        if len(newexres)!=0:
            
            for item in newexres:
                if time == 'Morning':
                    if item in morningList:
                        dealList = 'Morning'
                        del morningList[morningList.index(item)]
                        availabletimes = morningList
                if time == 'Afternoon':
                    if item in afternoonList:
                        dealList = 'Afternoon'
                        del afternoonList[afternoonList.index(item)]
                        availabletimes = afternoonList
                if time == 'Evening':
                    if item in eveningList:
                        dealList = 'Evening'
                        del eveningList[eveningList.index(item)]
                        availabletimes = eveningList
                if time == 'Night':
                    if item in nightList:
                        dealList = 'Night'
                        del nightList[nightList.index(item)]
                        availabletimes = nightList

        if availabletimes==0:
            if time == 'Morning':
                availabletimes = morningList
            elif time == 'Afternoon':
                availabletimes = afternoonList
            elif time == 'Evening':
                availabletimes = eveningList
            elif time == 'Night':
                availabletimes = nightList

        print(availabletimes)
        
        if len(availabletimes) == 0:
            messagebox.showerror('Search Failure','Sorry! But this room is unavailable for the selected day and time')
            return

        if self.numentries == 2:
            messagebox.showerror('Error','You can make 2 reservations per week. Try again next week')
            return

        
        self.homepage.withdraw()
        self.available.deiconify()

        Label(self.available, text='Building',relief=RAISED).grid(row=1,column=0,sticky=EW)
        Label(self.available, text='Floor',relief=RAISED).grid(row=1,column=1,sticky=EW)
        Label(self.available, text='Room',relief=RAISED).grid(row=1,column=2,sticky=EW)
        Label(self.available, text='Day',relief=RAISED).grid(row=1,column=3,sticky=EW)
        Label(self.available, text='Time',relief=RAISED).grid(row=1,column=4,sticky=EW)
        Label(self.available, text='Select',relief=RAISED).grid(row=1,column=5,sticky=EW)

        self.availableint = IntVar()
        row = 2
        value = 1
        for item in availabletimes:
            Label(self.available, text=building).grid(row=row,column=0)
            Label(self.available, text=floornumber).grid(row=row,column=1)
            Label(self.available, text=roomnumber).grid(row=row,column=2)
            Label(self.available, text=day).grid(row=row,column=3)
            Label(self.available, text=item).grid(row=row,column=4)
            
            Radiobutton(self.available, value=value, variable=self.availableint).grid(row=row,column=5)
            row = row + 1
            value = value + 1

        Button(self.available, text='Submit Reservation',command=self.makeReservation).grid(row=row, column=3, columnspan=2)
        Button(self.available, text='Cancel',command=self.AvailabletoHomepage).grid(row=row, column=5)

        self.availabletimes = availabletimes
        self.building = building
        self.floornumber = floornumber
        self.roomnumber = roomnumber
        self.day = day

        cursor.close()
        db.commit()
        db.close()
        
    def makeReservation(self):

        if self.availableint.get() == 0:
            messagebox.showwarning('Reservation Failure', 'Make sure to select an option or hit cancel')
            return

        insertTime = self.availabletimes[self.availableint.get() - 1]

        db = self.Connect()
        cursor = db.cursor()
        sql = 'INSERT INTO RoomReservations(Building, Floor, RoomNo, Day, Time, ReservedBy) VALUES (%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,(self.building,self.floornumber,self.roomnumber,self.day,insertTime,self.username))

        self.numentries = self.numentries + 1

        sql = 'UPDATE ReservationUser SET NumberOfReservations=%s WHERE Username=%s'
        cursor.execute(sql,(self.numentries,self.username))

        cursor.close()
        db.commit()
        db.close()

        messagebox.showerror('Reservation Completion','Congratulations! You have reserved your room. Click OK to go back to the Homepage')

        self.available.destroy()
        self.available = Toplevel()
        self.Homepage()
        self.AvailabletoHomepage()

    def AvailabletoHomepage(self):
        self.available.withdraw()
        self.homepage.deiconify()
        

    def cancelReservation(self):

        db = self.Connect()
        cursor = db.cursor()
        sql = 'DELETE FROM RoomReservations WHERE ReservedBy = %s'
        cursor.execute(sql,(self.username,))

        if self.numentries == 0:
            messagebox.showerror('Error!','You currently have 0 reservations!')
            return

        sql = 'UPDATE ReservationUser SET NumberOfReservations=%s WHERE Username=%s'
        cursor.execute(sql,(0,self.username))

        cursor.close()
        db.commit()
        db.close()


        messagebox.showerror('Cancellation Complete','You have canceled your previous reservation(s)')

        try:
            self.hpe2.destroy()
        except:
            pass
        
        self.Homepage()

    

    def stats(self):

        self.homepage.withdraw()
        self.statistics.deiconify()

        Label(self.statistics, text='The average number of reservations per person is:').grid(row=1,column=0)
        Label(self.statistics, text='The busiest building:').grid(row=2,column=0,sticky=W)

        self.statssv1 = StringVar()
        self.statse1 = Entry(self.statistics, textvariable=self.statssv1, width=50, state='readonly')
        self.statse1.grid(row=1,column=1,columnspan=2)

        self.statssv2 = StringVar()
        self.statse2 = Entry(self.statistics, textvariable=self.statssv2, width=50, state='readonly')
        self.statse2.grid(row=2,column=1,columnspan=2)

        backbutton = Button(self.statistics, text='Back',command=self.StatsToHomepage)
        backbutton.grid(row=3,column=2,sticky=EW)

        db = self.Connect()
        cursor = db.cursor()

        sql = 'SELECT * FROM RoomReservations'
        numreservations = cursor.execute(sql)

        sql = 'SELECT * FROM ReservationUser'
        numusers = cursor.execute(sql)

        avgres = numreservations/numusers
        self.statssv1.set(avgres)

        sql = 'SELECT COUNT(*), Building FROM RoomReservations GROUP BY Building'
        cursor.execute(sql)
        buildingList = cursor.fetchall()
        orderedbuildings = sorted(buildingList,reverse=True)

        if orderedbuildings[0][0] == orderedbuildings[1][0]:
            insertstr = 'Both are busy with ' + str(orderedbuildings[0][0]) + ' reservations so far'
            self.statssv2.set(insertstr)
        else:
            insertstr = str(orderedbuildings[0][1]) + ' is more busy with ' + str(orderedbuildings[0][0]) + ' reservations so far.'
            self.statssv2.set(insertstr)


    def StatsToHomepage(self):
        self.statistics.withdraw()
        self.homepage.deiconify()


    def HomepageToLogin(self):
        self.homepage.withdraw()
        self.login.deiconify()

    

login = Tk()
login.title('Login')

register = Toplevel()
register.title('Room Reservation New User Registration')

homepage = Toplevel()
homepage.title('Room Reservation Homepage')

available = Toplevel()
available.title('Available Rooms')

statistics = Toplevel()
statistics.title('Statistics')

app = Reservation(login,register,homepage,available,statistics)


login.mainloop()
