## by using  random making program  heads and tails
import random
import time
print("welcome to the coin toss program")
print("tossing the coin...")
time.sleep(2)
print("the result is...")
random_side = random.randint(0, 1)

if random_side == 1:
    print("heads")
else:
    print("tails")