import random


def game(p):
    if p == 'rock':
        if bot == 1:
            return print('Its a Tie')
        elif bot == 2:
            return print('You Lost')
        else:
            return print('You Won')

    if p == 'paper':
        if bot == 1:
            return print('You Won')
        elif bot == 2:
            return print('Its a Tie')
        else:
            return print('You Lost')

    if p == 'scissors':
        if bot == 1:
            return print('You Lost')
        elif bot == 2:
            return print('You Won')
        else:
            return print('Its a Tie')


bot = random.randint(1, 3)

p = input('choose : rock / paper / scissors : ')
if bot == 1:
    print('Bot Chose Rock')
elif bot == 2:
    print('Bot Chose Paper')
else:
    print('Bot Chose Scissors')

game(p)

# 1 = rock
# 2 = Paper
# 3 = scissors
