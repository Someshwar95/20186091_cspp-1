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
    #x = 25
    guess = s/2.0
    #guessesare = 0
    while abs(guess*guess - x) >= epsilon:
        #guessesare += 1 
        guess = guess - (((guess**2) - x)/(2*guess))
    #print('guessesare = ' + str(guessesare))
    #print('square root of ' + str(x) + 'is about ' + str(guess))
    print(guess)   

if __name__== "__main__":
    main()
