# Import random module
import random

print('Snake - Water - Gun')

# Input no. of rounds
n = int(input('Enter number of rounds: '))

# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0

# There will be n rounds of game
while rounds <= n:

    # Display round
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

    # Exception handling
    try:
        player = input("Chose your option: ")
    except EOFError as e:
        print(e)

    # Control of bad inputs
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue


    computer = random.choice(options)

    # Conditions based on the game rule
    if computer == 's':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1

    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1

    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1

    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")
    else:
        print("Draw!!\n")

    rounds += 1


if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")