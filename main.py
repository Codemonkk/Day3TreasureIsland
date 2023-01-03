print("Welcome to Treasure Island.")
print("Your mission is to find the treausre.")
dir = input('You\'re at a cross road. Where do you want to go? Type "left" or "right". ')
if dir == "left":
    print('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to swim across')
    new_dir = input()
    if new_dir == "swim":
        print("you get attacked by an angry trout. game over!")
    elif new_dir == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        color = input()
        if color == "red":
            print("game over!")
        elif color == "yellow":
            print("You win!")
        elif color == "blue":
            print("game over!")
        else:
            print("game over!")
else:
    print("You fell into a hole.Game Over.")