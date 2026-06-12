## the power of range in python
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)    

## practice problem

total = 0
for i in range(1, 101):
    total += i
print(total)

## fizz buzz problem game
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")    
    else:    
        print(i)
