import random
secret_number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100. Can you guess it?')
num_guesses = input('Pick your amount of guesses:')

guess = input('Enter you guess:')
num_guesses = int(num_guesses) - 1


while num_guesses >0:
   # print('Wrong guess. Number of guesses remaining:' + str(num_guesses))
    if int(guess) < secret_number:
        print('Guess a higher number! Number of guesses remaining:' + str(num_guesses))
        guess = input('Enter you guess:')
        num_guesses = int(num_guesses) - 1
    elif int(guess) > secret_number:
        print('Guess a lower number! Number of guesses remaining:' + str(num_guesses))
        guess = input('Enter you guess:')
        num_guesses = int(num_guesses) - 1
    elif int(guess) == secret_number:
        print('You won!')
        break
while num_guesses == 0:
    print('LOSER :(')
    break
    
