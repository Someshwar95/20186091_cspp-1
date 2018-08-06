'''
# Exercise: fourth power
# Write a Python function, fourthPower, that takes in one number
and returns that value raised to the fourth power.
# You should use the square procedure that you defined in an earlier
exercise exercise (you don't need to redefine square in this box;
# This function takes in one number and returns one number.
@author: Someshwar95
'''

def square(x_four):
    '''
    x: int or float.
    # Your code here
    '''
    return x_four**2

def fourth_power(x_four):
    '''
    x: int or float.
    # Your code here
    '''
    return x_four**4

def main():
    '''
    fourthpower
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
