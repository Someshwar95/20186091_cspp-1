'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
e=''
    ''.join(e for e in string if e.isalnum())
    print(e.isalnum())

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
