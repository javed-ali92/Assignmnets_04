import random

print('Welcome to Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount to password to generator: ')
number = int(number)


length = input('Input your password length:')
length = int(length)

print('\nhere are your password: ')


for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
print(password)