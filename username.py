import statics



def username(catch=None):
    usrObj = open("username", "r")

    for row in usrObj:
        statics.username = row

    if len(statics.username) < 2:
        statics.username = input("What is your name?: ")
        usrObj = open("username", "w")
        usrObj.write(statics.username)

username()