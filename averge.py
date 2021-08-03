'''def Melt_up(num_1, num_2):
    product = num_1 * num_2
    if product > 1000:
        return product
    else:
        return num_1 + num_2
number_1 =20
number_2 =40
print("\n")
result =Melt_up(number_1, number_2)
print("the result is ", result)
'''
'''
print("python range ()" "example")
print("get numbers from range 0 to 6")
for i in range(6):
    print(i, end='')
print("gets numbers from range 0  to 10")
i=0
while i <= 10:
    print(i, end='')
    i + 1
print("print pattern")
'''
'''
print("print pattern")
number =10
for row in range(1, number):
    for column in range(1, row+1):
       print(column, end='')
    print("")
    '''
'''
sum_2=0
num=int(input("enter a number"))
for i in range(1, num+ 1, 1):
   sum_2 +=1
   print("the given number is  ", str(sum_2))
number =0
'''

'''num_2=2
for i in range(1, 11, 1):
    product =num_2*i
    print(product)
    '''
list=[12, 13, 32, 42, 55, 122, 132, 150, 180, 200]
for num in list:
    if num > 200:
        break
    elif num % 5==0:
         print(num)

