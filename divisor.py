'''Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder'''
x=int(input("Give me a number: "))
d=[]
for n in range(1, x +1):
    if x % n==0:
      d.append(n)
    if len(d) ==2:
       print("Prime number")
else:
    print(d)

number =int(input("enter a number "))
divisor_list=[]
for num in range(1, number+1):
    if number % num==0:
        divisor_list.append(num)
print(divisor_list)
