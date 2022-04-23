# Uses python3
import sys,time

def get_change(m):
    #write your code here
    n_coins = 0
    while(m!=0):
        if m>=10:
            n_coins = n_coins + int(m/10)
            m = m%10
        elif m >= 5:
            n_coins = n_coins + int(m/5)
            m = m%5
        else:
            n_coins = n_coins + m
            m = m-m
    return n_coins

def get_change2(m):
    #write your code here
    n_coins = 0
    while(m>0):
        if m>=10:
            m -= 10
        elif m >= 5:
            m -= 5
        else:
            m -= 1
        n_coins = n_coins + 1

    return n_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
