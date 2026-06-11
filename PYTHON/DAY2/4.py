## small practice programe

print("--- welcome to the pizza shop ---")

name = input("what is your name? ")
size = input("what size of pizza do you want? (small/medium/large) ")
extra_cheese = input("do you want extra cheese? (yes/no) ")
total_bill = 0

if size == "small":
    total_bill += 15
elif size == "medium":
    total_bill += 20
elif size == "large":
    total_bill += 25
else:
    print("invalid input for size")
    exit()
    
if extra_cheese == "yes":
    total_bill += 2
elif extra_cheese == "no":
    total_bill += 0
else:
    print("invalid input for extra cheese")
    exit()      

print("\n----- BILL -----")
print(f"Customer : {name}")
print(f"Total Bill : ${total_bill}")
print("----------------")