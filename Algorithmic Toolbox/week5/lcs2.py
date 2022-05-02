#Uses python3

import sys

def lcs_(a,b,n,m,length):
    if n >= len(a) and m >= len(b):
        return length 
    q,w = n,m
    for i in range(n,len(a)):
        for j in range(m,len(b)):
            if a[i] == b[j]:
                if j >= w :
                    length = length + 1
                    q = i
                    w = j
                else:
                    pass
    #return lcs_(a,b,q+1,w+1,length)
    return length

    
def lcs2(a, b):
    #write your code here
    cost = 0
    for i in range(len(a)):
        lcs = lcs_(a,b,i,0,0)
        if lcs == None:
            continue
        if cost < lcs:
            cost = lcs
    return cost

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    """
    input = sys.stdin.readline()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    """
    print(lcs2(a, b))
