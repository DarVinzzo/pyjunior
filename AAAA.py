import random


user_turn = input('Your turn: ')

computer_choice = random.randint(1, 3)

# SAZAROJUMS

if computer_choice == 1:
    computer_turn = 'Rock'

if computer_choice == 2:
    computer_turn = 'Paper'

if computer_choice == 3:
    computer_turn = 'Scissors'


print(f'{user_turn} vs. {computer_turn}')


user_wins_1 = user_turn == 'Rock' and computer_turn == 'Scissors'
user_wins_2 = user_turn == 'Paper' and computer_turn == 'Rock'
user_wins_3 = user_turn == 'Scissors' and computer_turn == 'Paper'

user_wins = user_wins_1 or user_wins_2 or user_wins_3

if user_wins:
    print('User wins!')

elif user_turn == 'Scissors' and computer_turn == 'Rock':
    print('User loses!')

elif user_turn == 'Paper' and computer_turn == 'Scissors':
    print('User loses!')

elif user_turn == 'Rock' and computer_turn == 'Paper':
    print('User loses!')

elif user_turn == computer_turn:
    print('Draw')

else:
    print('what')