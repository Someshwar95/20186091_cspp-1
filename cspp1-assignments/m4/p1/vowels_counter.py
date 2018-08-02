'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
@author: Someshwar95
'''
def main():
    s = string(input())
    # the input string is in s
    # remove pass and start your code here
    Vowels = 0
    for x in s:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' x == 'u':
            Vowels += 1
            print('Vowels are: ' + str(Vowels))
    if __name__== "__main__":
    main()
