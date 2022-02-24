import mysql.connector
import getpass

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="passman"
)
#connects to database



Master_password = "password"
print("Enter your master password:")
Master_password_input = input()
#asks for master password before running


if Master_password_input == Master_password:
    print("\nYou are in")
else:
    print("\nThat's not the password")
    exit()

#makes sure that the password is right


print("1.add new password")
print("2.retrevie existing password")


add_new_assword = "1"
retrive_existing_password = "2"
add_or_retrive = input()
#adds or retrives existing passwords


if add_or_retrive == add_new_assword:
    print("Enter the app name:")
    Appname = input()
    print("Enter the used email:")
    Email = input()
    print("Enter the used password:")
    Passwords = input()
    mycursor = mydb.cursor()
    sql = "INSERT INTO passwords (Appname, Email, Passwords) VALUES (%s, %s, %s)"
    val = (Appname, Email, Passwords)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record insterted.")
if add_or_retrive == retrive_existing_password:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM passwords")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
#if conditions to know which option did the user choose