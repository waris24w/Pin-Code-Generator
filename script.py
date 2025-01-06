import random
import string
digit = string.digits
number = int(input('How man pin you want to generate: '))
length = int(input('Enter the pin length: '))

for num in range(number):
    pin = ''
    for digi in range(length):
        pin += random.choice(digit)
    print(num+1,pin)


