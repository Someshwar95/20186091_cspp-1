'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
number and returns the factorial of given number.
# This function takes in one number and returns one number.
@author: Someshwar95
'''

def factorial(n_fact):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_fact in (0, 1):
        return 1
    else:
        return n_fact * factorial(n_fact-1)

def main():
    '''
    factorial of n
    '''
    a_case = input()
    print(factorial(int(a_case)))

if __name__ == "__main__":
    main()
