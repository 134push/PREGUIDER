## the price distribution 

print("hello ! welcome to the amesumnet park")

name = input("what is your name? ")
age = int(input("what is your age? "))
height = float(input("what is your height in cm? "))
total_bill = 0
if height < 120:
    print("you are not allowed to enter the park because you are too short")
else:
    picture = input("do you want to take a picture? (yes/no) ")
    if picture == "yes":
        print("the price of the picture is $3")
        total_bill += 3
    
    if age < 12:
        print("Child ticket: $5")
        total_bill += 5
    elif age >= 12 and age < 65 : 
        print("Adult ticket: $10")
        total_bill += 10
    else:
        print("Senior ticket: $7")
        total_bill += 7

print(f"Total bill: ${total_bill}")
