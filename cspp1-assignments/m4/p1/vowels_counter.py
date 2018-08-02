'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
 For ex_lmample, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
@author: Someshwar95
'''
def main():
    '''
    Write a program that counts up the number of 
    vowels contained in the string s
    '''
    in_str = input()
    vowels_ow = 0
    for i in in_str:
        if i in "aieou":
            vowels_ow += 1
    print(vowels_ow)

    if __name__ == "__main__":
        main()