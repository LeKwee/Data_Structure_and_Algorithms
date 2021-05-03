'''
f(n) = f(n-1) + f(n-2)

0,1,1,2,3,5,8,13,21
'''

def fibo(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    return fibo(n-1)+fibo(n-2)



print(fibo(9))
