import zipfile
import string
import itertools
from threading import Thread

def crack(zip,pwd):
    try:
        zip.extracktall(pwd=str.encode(pwd))
        print("Success: Password is" + pwd)
    except:
        pass

zipFile = zipfile.ZipFile("C:\\Users\\Timo_Zuerner\\Desktop\\nezip.zip")
myLetters = string.ascii_letters + string.digits
for r in range(6):
    print("1")
    for x in map(''.join, itertools.product(myLetters, repeat=r)):
        t = Thread(target=crack, args=(zipFile, x))
        t.start()
