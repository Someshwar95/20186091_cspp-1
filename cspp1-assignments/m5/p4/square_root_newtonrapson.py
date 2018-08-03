'''
# Write a python program to find the square root of the given number
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    s = float(input())
    '''
    # epsilon and step are initialized
    # don't change these values
    '''
    epsilon = 0.01
    guess = s/2.0
    while abs(guess*guess - s) >= epsilon:
        guess = guess - (((guess**2) - s)/(2*guess))
    print(guess)   

if __name__== "__main__":
    main()
