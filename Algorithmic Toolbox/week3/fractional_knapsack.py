# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, values, weights):
    value = 0.
    # write your code here
    weight = np.array(weights)/np.array(values)
    weight = list(weight)
    while capacity>0 and len(values) != 0:
        max_weight = 0
        for i in range(len(weight)):
            if weight[i] > max_weight:
                max_weight = weight[i]
                index = i
        values[index] -= 1
        capacity -= 1
        value += weight[index]
        
        if values[index]==0:
            values.pop(index)
            weight.pop(index)
            weights.pop(index)
            

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = [3 ,50 ,60,20, 100,50,120,30]
    #data = [1, 1000, 500, 30]

    n, capacity = data[0:2]
    values_ = data[2:(2 * n + 2):2]
    weights_ = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights_, values_)
    print("{:.10f}".format(opt_value))
