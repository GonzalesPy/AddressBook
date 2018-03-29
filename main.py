#Coded by GonzalesPy...
#test
from time import sleep
import threading
from threading import Thread

import statics
from user import userdates
from chat import chat

print("Hello, " + statics.username)


userdates.userdates()




def start():
    print("Add new contact 'nc'")
    print("See all contacts 'ac'")
    print("Search for a contact 'sc'")
    print("Start chat session 'chat'")
    statics.handler = input()

    if statics.handler == "nc":
        name = input("Full name: ")
        number = input("Telephone number: ")

        nCObj = open("contacts.txt", "a")
        nCObj.write(name)
        nCObj.write(number)
        nCObj.write("\n")
        nCObj.close()

    if statics.handler == "ac":
        aCObj = open("contacts.txt")
        for line in aCObj:
            print (line.rstrip())
        aCObj.close()

    if statics.handler == "sc":
        searchContact = input("For which contact do you wanna search \n")
        sCObj = open("contacts.txt", "r")
        for row in sCObj:
            if searchContact in row:
                print ("\n--------------------------- \n" + row + "--------------------------- \n")
        sCObj.close()
    if statics.handler == "chat":
       t1 = Thread(target=chat.server)
       t2 =Thread(target=chat.client)
       t1.start()
       t2.start()
       while t1.is_alive:
            sleep(1)
            if statics.message == "exitchat":
                t2.stop
                t1.stop()



        #if statics.message == "exitchat":



start()

while statics.run:  #runs the main


    if statics.handler == "exit":
        statics.run = False
        print("Bye " + statics.username + " see you next time! ;)" )
    else:
        start()







