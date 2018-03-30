import string
from random import randint

zero = 0
password = ""
min_char = 8
max_char = 12
allchar =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!""#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

passwordLengh = randint(min_char, max_char)
print(passwordLengh)

for zero in range(passwordLengh):
    char_pickInt = randint(0, 93)
    password = password + allchar[char_pickInt]
    min_char = min_char + 1


print(password)