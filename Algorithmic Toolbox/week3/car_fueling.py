# python3
import sys
import numpy as np

def compute_min_refills(distance, tank, stops):
    # write your code here
    n_stop =0 
    if distance < tank:
        return 0
    if len(stops)==0 or stops[0] > m:
        return -1 
    laststop = 0
    while (len(stops) != 0):
        if len(stops) == 1:
            next_stop = distance
        else:
            next_stop = stops[1]
        

        if next_stop - stops[0] > tank:
            return -1 


        if next_stop-laststop <= tank:
            stops.pop(0)
        else:
            laststop = stops[0]
            n_stop += 1
            stops.pop(0)
    return n_stop


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d, m, _, *stops = map(int, sys.stdin.readline().split())
    print(compute_min_refills(d, m, stops))
