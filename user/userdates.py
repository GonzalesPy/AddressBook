import statics



def username(catch=None):
    usrObj = open("userdates", "r")

    for row in usrObj:
        statics.username = row

    if len(statics.username) < 2:
        statics.username = input("What is your name?: ")
        statics.myphone = input("Your phone number: ")
        usrObj = open("userdates", "w")
        usrObj.write(statics.username)
        usrObj.write(statics.myphone)

username()