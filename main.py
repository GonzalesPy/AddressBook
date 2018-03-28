#Coded by GonzalesPy...

import Statics



print("Hello, " + Statics.username)



def start():
    print("Add new contact 'nc'")
    print("See all contacts 'ac'")
    print("Search for a contact 'sc")
    Statics.handler = input()

    if Statics.handler == "nc":
        name = input("Full name: ")
        number = input("Telephone number: ")

        nCObj = open("contacts.txt", "a")
        nCObj.write(name)
        nCObj.write(number)
        nCObj.write("\n")
        nCObj.close()

    if Statics.handler == "ac":
        aCObj = open("contacts.txt")
        for line in aCObj:
            print (line.rstrip())
        aCObj.close()

    if Statics.handler == "sc":
        searchContact = input("For which contact do you wanna search \n")
        sCObj = open("contacts.txt", "r")
        for row in sCObj:
            if searchContact in row:
                print ("\n--------------------------- \n" + row + "--------------------------- \n")
        sCObj.close()



start()  #start sc/nc

while Statics.run:  #runs the main


    if Statics.handler == "exit":
        Statics.run = False
        print("Bye " + Statics.username + " see you next time! ;)" )
    else:
       start()







