'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

def main():
    '''
    program for print the number of bob.
    '''
    s_case = input()
    num = 0
    for u_lkj in range(len(s_case)):
        if s_case[u_lkj:u_lkj+3] == "bob":
            num += 1
    print(num)

if __name__== "__main__":
    main()
