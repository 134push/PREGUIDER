## random password genrator easy 
import random
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]

print("Welcome to the password generator!")
num_letters = int(input("How many letters  and number  would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num = [num_letters, num_numbers, num_symbols] 
password1 = ""
for i in range(1, num[0] + 1):
    password1 += random.choice(letters)
for i in range(1, num[1] + 1):
    password1 += random.choice(numbers)
for i in range(1, num[2] + 1):
    password1 += random.choice(symbols)
print(f"Your password is: {password1}")

##  random password genrator hard

import random
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]

password = ""
print("Welcome to the password generator!")
num_letters = int(input("How many letters  and number  would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num = [num_letters, num_numbers, num_symbols] 
password_list = []
for i in range(1, num[0] + 1):
    password_list.append(random.choice(letters))
for i in range(1, num[1] + 1):
    password_list.append(random.choice(numbers))
for i in range(1, num[2] + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
for i in password_list:
    password += i

print(f"your password is {password}")    