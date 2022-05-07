# Uses python3
import sys
import itertools
import numpy as np

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight_dp2(W,w):
    max_result = 0 
    result = 0 
    for _, *c in itertools.product(range(3), repeat=len(w)):
        result = 0
        for  i in c:
            result += w[i]
            if result > W:
                break
            if result < W and max_result < result:
                max_result = result
    return max_result


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_dp2(W, w))
    
