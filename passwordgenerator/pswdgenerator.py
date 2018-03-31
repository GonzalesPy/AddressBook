from random import randint

zero = 0
password = ""
min_char = int (input("Minimum password lengh: "))
max_char = int (input("Maximum password lengh: "))
allchar =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!""#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

passwordLengh = randint(min_char, max_char)

for zero in range(passwordLengh):
    char_pickInt = randint(0, 92)
    password = password + allchar[char_pickInt]
    min_char = min_char + 1


print(password)
