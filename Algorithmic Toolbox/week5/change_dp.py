# Uses python3
import sys

# 사용하는 코인 : 4, 3, 1

def get_coin(n,x):
    remain = x%4
    if n > 1:
        if remain==1:
            return n + 1
        elif remain==2:
            return n + 1
        elif remain==3:
            return n + 1
        else:
            return n
    if remain==1:
        return 1
    elif remain==2:
        return 2
    elif remain==3:
        return 1
    else:
        return n


def get_change(m):
    #write your code here
    n_coin = m//4
    return get_coin(n_coin,m)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
