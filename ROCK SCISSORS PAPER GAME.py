import random

user_name = input ('Enter name:')

user_turn = input('Your turn: ')

computer_choice = random.randint(1, 3)

# PC CHOICES
if computer_choice == 1:
    computer_turn = 'Rock'

if computer_choice == 2:
    computer_turn = 'Paper'

if computer_choice == 3:
    computer_turn = 'Scissors'

# ? VERSUS ?
print(f'{user_turn} vs. {computer_turn}')
# WINS
user_wins_1 = user_turn == 'Rock' and computer_turn == 'Scissors'
user_wins_2 = user_turn == 'Paper' and computer_turn == 'Rock'
user_wins_3 = user_turn == 'Scissors' and computer_turn == 'Paper'

if user_wins_1 or user_wins_2 or user_wins_3:
    print(user_name + ' wins!')

# LOSES
user_lose_1 = user_turn == 'Scissors' and computer_turn == 'Rock'
user_lose_2 = user_turn == 'Paper' and computer_turn == 'Scissors'
user_lose_3 = user_turn == 'Rock' and computer_turn == 'Paper'

if user_lose_1 or user_lose_2 or user_lose_3 :
    print (user_name + ' lose!')

elif user_turn == computer_turn :
    print ('DRAAAAW!')

else:
    print ('eeh what is '+ user_turn + ' ?')