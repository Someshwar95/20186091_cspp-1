'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
'''

def main():
	'''
	# the input string is in s
	# remove pass and start your code here
	'''
	x = 'abxyzurs'
	b = ''
	d = ''
	for char in x:
		if (d == ''):
			d = char
		elif (d[-1] <= char):
			d = d+char
		elif(d[-1]>char):
			if (len(b)<len(d)):
				b=d
				d=char
			else:
				d=char
	if (len(d) > (b)):
		b=d
	print(b)

		
if __name__== "__main__":
	 main()
