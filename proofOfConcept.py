#Proof Of Concept

import pymysql

db = pymysql.connect(host='academic-mysql.cc.gatech.edu',user='cs4400_Group_41',
                     db='cs4400_Group_41',passwd='YIBz9hoA')

cursor = db.cursor()
sql = 'SELECT Username FROM User'
result = cursor.execute(sql)
# result carries the value of the number of tuples that will be affected by the SQL statement

usernames = cursor.fetchall()
print(usernames)
