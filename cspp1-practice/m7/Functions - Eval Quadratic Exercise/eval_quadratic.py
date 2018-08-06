'''
# Exercise: eval quadratic
# Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.
'''
def eval_quadratic(a_qu, b_ad, c_ra, x_tic):
    '''
    eval quadratic
    '''
    return a_qu*x_tic**2+b_ad*x_tic+c_ra

def main():
    '''
    eval quadratic
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_eva in range(len(data)):
        temp = str(data[x_eva]).split('.')
        if temp[1] == '0':
            data[x_eva] = int(float(str(data[x_eva])))
        else:
            data[x_eva] = data[x_eva]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
