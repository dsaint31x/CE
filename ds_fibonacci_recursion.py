import sys
def fibonacci(N):
    ret_v = -1
    # The above two if statements can be combined as:
    if N <= 1:
        ret_v = N
    else:
        ret_v = fibonacci(N - 1) + fibonacci(N - 2) 

    return ret_v 


if __name__ == '__main__':
    argc = len(sys.argv)
    N = -1
    if argc == 1:
        N = 7
    elif argc == 2:
        N = sys.argv[1]
    else:
        print(f'Error : program usage : {sys.argv[0]} N')
        print('N shoud be positive intenger.')
    
    print('---------------------')
    for i in range(N):    
        print(fibonacci(i+1))