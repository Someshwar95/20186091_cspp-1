'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
 For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
@author: Someshwar95
'''
def main():
    s_str = input()
    '''
    Write a program that counts up the number of 
    vowels contained in the string s
    '''
    Vowels_ow = 0
    for x in s_str:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            Vowels_ow += 1
    print('Vowels_ow are: ' + str(Vowels_ow))

 if __name__ == "__main__":
        main()