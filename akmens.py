import random

user_name = input ('Enter name:')

user_turn = input('Your turn: ')

computer_choice = random.randint(1, 3)


if computer_choice == 1:
    computer_turn = 'Rock'

if computer_choice == 2:
    computer_turn = 'Paper'

if computer_choice == 3:
    computer_turn = 'Scissors'

print(f'{user_turn} vs. {computer_turn}')

if user_turn == 'Rock' and computer_turn == 'Scissors':
    print(user_name + ' wins!')

if user_turn == 'Paper' and computer_turn == 'Rock':
    print(user_name + ' wins!')

if user_turn == 'Scissors' and computer_turn == 'Paper':
    print(user_name + ' wins!')

if user_turn == 'Scissors' and computer_turn == 'Rock':
    print(user_name + ' Lose!')

if user_turn == 'Rock' and computer_turn == 'Paper':
    print(user_name + ' Lose!')

if user_turn == 'Paper' and computer_turn == 'Scissors':
    print(user_name + ' Lose!')

if user_turn == computer_turn :
    print ('DRAAAAW!')



