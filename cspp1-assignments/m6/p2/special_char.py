'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str1_input = ""
    for char in str_input:
        if char in'!@#$%^&*':
            str1_input += " "
        else:
            str1_input += char
    print(str1_input)

if __name__ == "__main__":
    main()
