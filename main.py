from Admin import *
from Official import *
from show_db import *
###dbms connection

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    password = "mypass",
    database = "criminalrecord"

)

mycursor = mydb.cursor()

def main():
    while 1:
        print("Criminal Record of Dhaka City")
        print("")
        print("1. Login as Official")
        print("2. Login as Admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_official()
        elif user_option == "2":
            auth_admin()
        else:
            print("No valid option was selected")

main()