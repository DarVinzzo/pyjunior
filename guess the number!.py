import random

random_number = random.randint(0, 150)
print(random_number)

# while atkārto kodu, kamēr nosacījums patiess

guessing_number = True
guesses = []
# jāpadara guessing_number par False
# kad uzminējām skaili
while guessing_number:

    user_guess = int(input('Guess the number: '))

    # vai ir lielāks
    if user_guess > random_number:
        print('Your guess is larger than my number')
        guesses.append(user_guess - random_number)

    # vai ir mazāks
    elif user_guess < random_number:
        print('Your guess is lesser than my number')
        guesses.append(random_number - user_guess)

    else: # šis izpildās kad uzmin skaitli
        # kad lietotājs uzmin, while tiek pārtraukts
        print('You guessed my number!')
        guessing_number = False

# aprēķinu cik vidēji tālu biju no patiesības
print(f'Average deviation: {sum(guesses) / len(guesses)}') # aprēķināt vidējo
print(f'Total amount of guesses: {len(guesses)}') 