'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
special = '''!$#@'''
def clean_string(string):
out = ""
	for char in input():
		if char not in special:
			out = out + char
	print(out)

    

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
