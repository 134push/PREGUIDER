## basic printing methods
print("hello sir/ma'am how can i help you?")
name = input("what is your name? ")

## by using f string
print("hello " + name + " how are you doing?")

## basic methods of string

print("hello"[0]) ## it will print the first letter of the string
print("123" + "456") ## it will concatenate the two strings and print 123456
print("hello " * 3) ## it will print the string hello three times

## basic methods of numbers

print(2 + 3) ## it will print 5
print(int("1230") + 3) ## it will print 1233

## basic maths operations

print( 10 / 13) ## it will print 0.7692307692307693 because it is the division operator
print(10 // 3) ## it will print 3 because it is the floor division operator
print(10 % 3) ## it will print 1 because it is the modulus operator
print(10 ** 3) ## it will print 1000 because it is the exponentiation operator
print(2^2) ## it will print 0 because it is the bitwise XOR operator

m = 2.6 + 56
print(int(m))## it will print 58 because it will convert the float to an integer by truncating the decimal part
print(round(m))## it will print 59 because it will round the float to the nearest integer