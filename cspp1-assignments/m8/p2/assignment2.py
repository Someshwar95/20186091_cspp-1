'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in
one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
@author: Someshwar95
'''
def sumofdigits(n_sum):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_sum > 0:
        return n_sum % 10 + sumofdigits(n_sum//10)
    return 0

def main():
    '''
    sum of digits
    '''
    a_dig = input()
    print(sumofdigits(int(a_dig)))

if __name__ == "__main__":
    main()
