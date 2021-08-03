import random

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c' and low != high:
        if low != high:
            guess=random.randint(low, high)
        else:
            guess=low
        feedback = input(f' is {guess}  to high(H) and to low(L)  or correct(C)').lower()
        if feedback =='h':
            guess=high-1
        elif feedback =='l':
            guess=low+1
    print(f'yay your computer guessed number  {guess} correctly')
computer_guess(10)
