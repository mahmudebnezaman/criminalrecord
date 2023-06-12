import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "mypass",
database = "criminalrecord"
)
mycursor = mydb.cursor()

def update_session():
    while 1:
        print("")
        print("Select a option")
        print("1. Name")
        print("2. Age")
        print("3. Sex")
        print("4. Date of birth")
        print("5. NID")
        print("6. Birth Certificate Number")
        print("7. Birth Mark")
        print("8. Crime Type")
        print("9. Sentenced Punishment")
        print("10. Back")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            sn = input(("Serial No : "))
            nm = input(("Name : "))
            query_vals = sn, nm

            mycursor.execute("UPDATE `record` SET `Name`='%s' WHERE `Serial_No`= %s",query_vals)
            mydb.commit()
            print("Record has updated")
        elif user_option == "2":
            print("")

            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Age: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Age`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")
            #try:
                #mycursor.execute("UPDATE `record` SET `Age`= %s WHERE `Serial_No`= %s", query_vals)
                #mydb.commit()
                #print("Record has updated")
            #except:
                #print("Record Was not Found")
            
        elif user_option == "3":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Sex: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Sex`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "4":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New DOB: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Date_Of_Birth`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "5":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New nid: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `NID`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "6":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Birth Certificate: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Birth_Cirt`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "7":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Birth Marks: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Birth_Mark`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "8":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Crime Type: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Crime_Type`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "9":
            print("")
            sn = input(("Enter the Serial No of a criminal  : "))

            nm = input("Enter New Sentenced Punishment: ")
            query_vals = nm, sn
            mycursor.execute("UPDATE `record` SET `Sentenced_Punishment`= %s WHERE `Serial_No`= %s", query_vals)
            mydb.commit()
            print("Record has updated")

        elif user_option == "10":
            break
        else:
            print("No valid option selected")