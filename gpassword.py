import random
import string
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass_len = 24
p ="".join(random.sample(s, pass_len))
print(p)

def pass_word():
    password= ''
    count = 0
    length = int(input("How many characters would you like in your password? "))
    while count != length:
        upper =[random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol
        password += random.choice(everything)
        count += 1
        pass
    if count == length:
       print(password)
print(pass_word())