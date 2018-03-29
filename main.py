#Coded by GonzalesPy...
#test
import statics
import username


print("Hello, " + statics.username)


username.username()



def start():
    print("Add new contact 'nc'")
    print("See all contacts 'ac'")
    print("Search for a contact 'sc")
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



start()  #start sc/nc

while statics.run:  #runs the main


    if statics.handler == "exit":
        statics.run = False
        print("Bye " + statics.username + " see you next time! ;)" )
    else:
       start()







