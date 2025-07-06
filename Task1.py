n=int(input('Enter a number: '))

def factorial(n):
    if(n<=2):
        return n
    else:
        return n * (factorial(n-1))

ans = factorial(n)
print('Factorial of',n,'is:',ans)