from data_manager import *


dm = DataManager()
flag = True
while flag:
    print("---------------Welcome to Flight Club-------------")
    fname = input("Enter your first name:\n>>> ")
    lname = input("Enter your last name:\n>>> ")
    Email = input("Enter your email:\n>>> ")
    REmail = input("Re-enter youe email:\n>>> ")
    if(Email==REmail):
        flag = False
        dm.set_user(fname=fname,lname=lname,email=Email)
        print("You are our user now....")
    else:
        print("Wrong Input...")