## find trseure 
0
print("""
🏝️ TREASURE ISLAND MAP 🏝️

        🌊 🌊 🌊 🌊 🌊 🌊 🌊
     🌊  🟩 🟩 🟩 🟩 🟩  🌊
     🌊  🟩 🌴 🟩 🪨 🟩  🌊
     🌊  🟩 🟩 🏚️ 🟩 🟩  🌊
     🌊  🟩 🐍 🟩 💰 🟩  🌊
     🌊  🟩 🟩 🟩 🌴 🟩  🌊
        🌊 🌊 🌊 🌊 🌊 🌊 🌊

Legend:
🌊 = Water
🟩 = Land
🌴 = Tree
🪨 = Rock
🏚️ = Old Hut
🐍 = Danger
💰 = Treasure
""")

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "right":
        print("You've chosen the right path.")
else:
        print("You've chosen the left path.")
        choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
        if choice2 == "wait":
                print("You waited for a boat and safely reached the island.")
                choice3 = input("You see three doors: one red, one yellow, and one blue. Which door do you choose? ").lower()
                if choice3 == "yellow":
                        print("Congratulations! You found the treasure! 🏆")
                elif choice3 == "red":
                        print("It's a trap! You were burned by fire. Game Over. 🔥")