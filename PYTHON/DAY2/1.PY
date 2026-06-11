## CONDITIONAL STATEMENTS

print("Enter your age: ")
age = int(input()) ## it will take the input from the user and convert it to an integer 
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")        