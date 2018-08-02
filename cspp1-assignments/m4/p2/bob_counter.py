'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

def main():
    s = input()
    '''
    # the input string is in s
    # remove pass and start your code here
    '''
    num = 0
    for u in range(len(s)):
        if s[u:u+3] == "bob":
            num += 1
            print('num are: ' + str(num))

if __name__== "__main__":
    main()
