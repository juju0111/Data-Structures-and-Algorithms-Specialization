# python3

import time 
def max_sliding_window_naive(sequence, m):
    maximums = []

    for i in range(len(sequence) - m +1):
        maximums.append(max(sequence[i:m+i]))

    return maximums


def max_sliding_window(sequence, m):
    maximums = []
    queue = [sequence[i] for i in range(m)]
    max_n = max(queue)
    maximums.append(max_n)

    for i in range(1,len(sequence) - m +1):
        last_ele = queue.pop(0)
        new_ele = sequence[m+i-1]
        queue.append(new_ele)
        
        if new_ele > max_n or last_ele == max_n:
            max_n = max(queue)
        
        maximums.append(max_n)

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))

