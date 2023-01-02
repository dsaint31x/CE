import sys
def main(n):
    first = 0
    second = 1
    tmp = first+second
    
    cnt = 0
    # print(second)
    while cnt < n:
        print(second)
        first = second
        second = tmp
        tmp = first+second
        cnt += 1
        
if __name__ == '__main__':
    argc = len(sys.argv)
    n = -1
    if argc == 1:
        n = 7
    elif argc == 2:
        n = sys.argv[1]
    else:
        print(f'Error : program usage : {sys.argv[0]} N')
        print('N shoud be positive intenger.')
    
    main(n)    
        
        
         