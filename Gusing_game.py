import random

def guss(y):

    random_number=random.randint(1, y)
    guess=0
    while guess !=random_number:
        guess=int(input(f'enter guessing number between 0 and {y}'))
        if guess < random_number:
            print(f'the guessing number is to low')
        elif guess > random_number:
            print(f'the guessing number is to high')

    print(f'congrats you guessed the number {random_number}')
guss(10)







