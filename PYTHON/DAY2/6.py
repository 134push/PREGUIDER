## find trseure small practice progrme
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

print("welcome to the treasure island")
print("your mission is to find the treasure")

choice1 = input("you are at a cross road, where do you want to go? (left/right) ")
if choice1 == "right":
        print("you fell into a hole. game over.")
        exit()

elif choice1 == "left":
        choice2 = input("you come to a lake. there is an island in the middle of the lake. do you want to wait for a boat or swim across? (wait/swim) ")
        if choice2 == "swim":
                print("you get attacked by an angry trout. game over.")
                exit()
        elif choice2 == "wait":
                choice3 = input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose? (red/yellow/blue) ")
                if choice3 == "red":
                        print("it's a room full of fire. game over.")
                        exit()
                elif choice3 == "yellow":
                        print("you found the treasure! you win!")
                elif choice3 == "blue":
                        print("you enter a room of beasts. game over.")
                        exit()
                else:
                        print("you chose a door that doesn't exist. game over.")
                        exit()
        else:
                print("invalid input for lake choice. game over.")
                exit()        