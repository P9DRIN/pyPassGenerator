import string
import random

upper = string.ascii_uppercase
num = string.digits
lower = string.ascii_lowercase
symbols = string.punctuation
hexDigits = string.hexdigits

length = int(input('Enter the length of password here: '))


while length:
    if length <= 8:
        all = hexDigits + num
        temp = random.sample(all, length)
        password = "".join(temp)
        print(password)
        break
    elif length <= 16:    
        all = hexDigits + symbols + symbols + upper
        temp = random.sample(all, length)
        password = "".join(temp)
        print(password)
        break
    elif length <= 22:
        all = hexDigits + hexDigits + upper + lower + num + symbols
        temp = random.sample(all, length)
        password = "".join(temp)
        print(password)
        break
    elif length >= 23:
        print('Error! Must be a number between 1 and 22')
        break

