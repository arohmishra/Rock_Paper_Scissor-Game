import random

game = ['r','p','S']
# print(f"{game}")

user_input = input("choose r for rock, p for paper, and s for scissor : ")

game_output = random.choice(game)

print(f"computer choice = {game_output}\n your choice = {user_input}")

if user_input == 'r' and game_output == 's':
    print("you win")
elif user_input == 'p' and game_output == 'r':
    print("you win")
elif user_input == 's' and game_output == 'p':
    print("you win")    
elif game_output == user_input :
    print("play again..")    
else :
    print("you lose,\n Better luck next time 😊")    