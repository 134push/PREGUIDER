import random
num1 = [1,3,5,7,9]
num2 = [2,4,6,8,10]
num = random.randint(0, len(num1) - 1)
print(f"The random number is: {num}")
print(f"The random number is: {num1[num]}")

number = [num1, num2]
print(number)

print(num1[:-1])
print(num1[1:4])
print(num1[::2])## print every second element in the list
print(num1[::-1])## reverse the list