#wapp to read username password
import getpass
username=input("Enter user name =")

Password=getpass.getpass("Enter password =")

if username=="antman" and Password=="batman":
    print("Welcome")
else:
    print("try again")
    