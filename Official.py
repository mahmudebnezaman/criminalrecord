import show_db

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypass",
    database="criminalrecord"
)
mycursor = mydb.cursor()


def auth_official():
    print("")
    print("Official Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "official":
        if password == "password":
            official_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")


def official_session():

    while 1:

        print("")
        print("Offical Menu")
        print("1. Show full Criminal Record")
        print("2. Search For a record")
        print("3. Logout")

        user_option = input(str("Option : "))

        if user_option == "1":
            print("")
            print("Full Criminal Record")
            show_db.show_record()
            # Show Criminal Record

        elif user_option == "2":
            print("")
            print("Search for a Record")

            sn = input(("Serial No : "))
            nm = input(("Name : "))
            query_vals = sn, nm

            mycursor.execute("SELECT * FROM record WHERE Serial_No = %s AND Name= %s",query_vals)
            for x in mycursor:
                print(x)
            mydb.commit()
            print(mycursor.rowcount, "Records are shown.")
            # add record


        elif user_option == "3":
            break
        else:
            print("No valid option selected")
            print("")
