#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    #data = [1, 23, 39]
    #data = [3 , 1, 3, -5, -2,4,1]
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]

   
    print(max_dot_product(a, b))
    
