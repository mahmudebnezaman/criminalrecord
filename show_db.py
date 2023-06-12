
import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root" ,
password = "mypass" ,
database = "criminalrecord"
)
mycursor = mydb.cursor()

def show_record():
    sql = "SELECT * FROM `record`"
    mycursor.execute(sql)
    print("(`Serial_No`, `Name`, `Age`, `Sex`, `Date_Of_Birth`, `NID`, `Birth_Cir`, `Birth_Mark`, `Crime_Type`, `Sentenced_Punishment`)")
    for x in mycursor:
        print(x)
    mydb.commit()
    print(mycursor.rowcount, "Records are shown.")
