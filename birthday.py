import time
'''price_dic={"banana": 1, "mango": 3, "orange": 4, "apple": 5}
print(price_dic.keys())
age=int(input("enter your age "))
print("your age is ", age)
birth_day={"age": 12}
'''


'''if __name__ == '__main__':

    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
        '''


Birthdays = {
            "Albert Einstein": "14/3/1889",
            "Bill Gates": "28/10/1955",
            "Steve Jobs": "24/2/1955",
        }
print("Welcome to the Birthday game ! We have the birthdays to:")
time.sleep(1)
for x in Birthdays:
    print(x)
    time.sleep(0.7)
    choice = input("\nWho's birthday do you want to look up?")

if choice in Birthdays:
    print("The birthday of {} is: ".format(choice))
    print(Birthdays[choice])
