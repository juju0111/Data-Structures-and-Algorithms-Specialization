# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    max_ele = a[left]
    max_cnt = 1
    ele = a[0]
    cur_cnt = 1
    for i in range(left+1,right):
        if a[i] == ele:
            cur_cnt += 1
        else:
            if cur_cnt > max_cnt:
                max_ele = ele
                max_cnt = cur_cnt
            ele = a[i]
            cur_cnt = 1

    if cur_cnt > max_cnt:
        max_ele = ele
        max_cnt = cur_cnt
        
    if max_cnt > (left-right):
        return max_ele

    return -1 

def get_majority_element_divandconq(a, left, right):
    # last tree level
    if (right - left) == 1:
        return a[left]
    else:
        a.sort()
        # split point
        mid = (left + right) // 2

        left_maj_elem = get_majority_element(a, left, mid)
        right_maj_elem = get_majority_element(a, mid+1, right)

        # define whether there is a majority element for the part of the array
        # majority elements, exclude -1
        maj_elems = (a for a in (left_maj_elem, right_maj_elem) if a != -1)
        for maj_elem in maj_elems:
            cnt = 0
            for i in range(left, right):
                if a[i] == maj_elem:
                    cnt += 1
            if cnt > (right - left) / 2:
                return maj_elem
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_divandconq(a, 0, n) != -1:
        print(1)
    else:
        print(0)
