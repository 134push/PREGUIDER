## practice program for the whoes pays the bill
import random
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

## choice use for randomly select an item from a list
friend_who_will_pay = random.choice(friends)
print(f"{friend_who_will_pay} will pay the bill.")

random.shuffle(friends)
print(friends)