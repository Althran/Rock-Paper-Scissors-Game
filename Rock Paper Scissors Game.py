import random

s = 'y'
p = 0
c = 0
stack = ['rock', 'scissors', 'paper']

while s == 'y':
    print('Please, enter rock/scissors/paper')
    player = str(input())
    computer = stack[random.randint(0, len(stack) - 1)]
    if player == computer:
        print('Tie, try again')
    elif player == 'rock' and computer == 'scissors':
        print('Player win')
        p += 1
    elif player == 'rock' and computer == 'paper':
        print('Computer win')
        c += 1
    elif player == 'scissors' and computer == 'rock':
        print('Computer win')
        c += 1
    elif player == 'scissors' and computer == 'paper':
        print('Player win')
        p += 1
    elif player == 'paper' and computer == 'rock':
        print('Player win')
        p += 1
    elif player == 'paper' and computer == 'scissors':
        print('Computer win')
        c += 1
    elif player != 'paper' or 'scissors' or 'rock':
        print('You write wrong word, please try again.')
    print('Continue? y/n')
    s = input()
print('Finale score: Player:', p, '/', 'Computer:', c)
