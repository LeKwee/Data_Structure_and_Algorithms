'''
Write a program that prints the number from 1 to 100.
For multiples of 3, print "Fizz" instead.
For multiples of 5, print "Buzz" instead.
for numbers which are multiples of both, print "FizzBuzz".
'''

'''
Methoh 1
'''
# for i in range(1,101):
#     factor_of_three = False
#     factor_of_five = False

#     if i%3 == 0:
#         factor_of_three = True
#     if i%5 == 0:
#         factor_of_five = True

#     if factor_of_five and factor_of_three:
#         print(str(i) + " FizzBuzz")
#         factor_of_five = False
#         factor_of_three = False
#     elif factor_of_three:
#         print(str(i) +  " Fizz")
#         factor_of_three = False
#     elif factor_of_five:
#         print(str(i) +  ' Buzz')
#         factor_of_five = False
#     else:
#         print(i)

'''
Methoh 2
'''
# for i in range(1,101):
#     fizz = 'Fizz' if i%3==0 else ''
#     buzz = 'Buzz' if i%5==0 else ''
#     print(f'{i} {fizz}{buzz}')

'''
Method 3
'''
[print("Fizz"*(not i%3) + "Buzz"*(not i%5)) or print(i) for i in range(1, 100)]