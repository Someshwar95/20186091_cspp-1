'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
    	if item in my_dict:
    		my_dict[item] += 1
    	else:
    		my_dict[item] = 1
    print(my_dict)
            
def main():
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
