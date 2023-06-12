import show_db
import update_db
import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root" ,
password = "mypass" ,
database = "criminalrecord"
)
mycursor = mydb.cursor()

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":

            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")


def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Show full Criminal Record")
        print("2. Add a new Criminal Record")
        print("3. Update Existing Criminal Record")
        print("4. Delete Existing Record")
        print("5. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Full Criminal Record")
            show_db.show_record()
            #Show Criminal Record

        elif user_option == "2":
            print("")
            print("Add a new Criminal Record")

            #sl_no = input(str("S : "))
            nm = input(str("Name: "))
            ag = input(str("Age: "))
            sx = input(str("Sex: "))
            dob = input(str("Date of Birth(DD-MM-YYYY): "))
            nid1 = input(str("NID NO.: "))
            bc = input(str("Birth Certificate NO.: "))
            bm = input(str("Birth Mark: "))
            ct = input(str("Crime Type: "))
            sp = input(str("Sentenced Punishment : "))
            query_vals = (nm,ag,sx,dob,nid1,bc,bm,ct,sp)
            mycursor.execute("INSERT INTO `record` (`Serial_No`,`Name`, `Age`, `Sex`, `Date_Of_Birth`, `NID`, `Birth_Cirt`, `Birth_Mark`, `Crime_Type`, `Sentenced_Punishment`) VALUES ('',%s,%s,%s,%s,%s,%s,%s,%s,%s)",query_vals)
            mydb.commit()
            print("New record has been registered")

            #add record

        elif user_option == "3":
            print("")
            print("Update Existing Existing Criminal Record")
           #call update function
            update_db.update_session()


        elif user_option == "4":
            print("")
            print("Delete Existing Criminal Record")
            sn = input("Serial No : ")
            nm = input("Name = ")
            query_vals = sn,nm
            mycursor.execute("DELETE FROM `record` WHERE Serial_no = %s and Name = %s",query_vals)
            mydb.commit()
            if mycursor.rowcount < 1:
                print("Record not found")
            else:
                print(sn + " has been deleted")

        elif user_option == "5":
            break
        else:
            print("No valid option selected")