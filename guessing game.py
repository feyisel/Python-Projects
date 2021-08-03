import random

print("number guessing game ")
chances =0
number =random.randint(1, 10)
print("guess number (between1, 10):")

while chances < 5:
    guess =int(input())
    if chances==number:
        print("congrats you win")
    elif chances < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("your guess was to high guess a number lower than ", guess)
        chances +=1
    if not chances < 5:
        print("you lose the number", number)





