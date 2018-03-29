import statics



def userdates():
    usrObj = open("C:\\Users\\Timo_Zuerner\\PycharmProjects\\AddressBook\\user\\userdates", "r")

    for row in usrObj:
        statics.username = row

    if len(statics.username) < 2:
        statics.username = input("What is your name?: ")
        statics.myphone = input("Your phone number: ")
        usrObj = open("C:\\Users\\Timo_Zuerner\\PycharmProjects\\AddressBook\\user\\userdates", "w")
        usrObj.write(statics.username + "\n")
        usrObj.write(statics.myphone)


