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
    s_str = input()
    vowels_ow = 0    
    for x_lm in s_str:
        if x_lm == 'a' or x_lm == 'e' or x_lm == 'i' or x_lm == 'o' or x_lm == 'u':
            vowels_ow += 1
    print('vowels_ow are: ' + str(vowels_ow))

    if __name__ == "__main__":
        main()