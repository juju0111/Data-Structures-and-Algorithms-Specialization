# Uses python3

#!pip3 install numpy

import numpy as np

def edit_distance(s, t):
    #write your code here
    D=np.zeros((len(s)+1,len(t)+1))

    for i in range(len(s)+1):
        D[i,0] = i
    for i in range(len(t)+1):
        D[0,i] = i

    for j in range(1,len(t)+1):
        for i in range(1,len(s)+1):
            insertion = D[i,j-1] + 1
            deletion = D[i-1,j] + 1
            match = D[i-1,j-1]
            mismatch = D[i-1,j-1] + 1
            if s[i-1] == t[j-1]:
                D[i,j] = min(insertion,deletion,match)
            else:
                D[i,j] = min(insertion,deletion,mismatch)   
 
    return output_alignment(D,len(s),len(t),s,t,0)  

def back_track(D,i,j):
    k = i-1
    l = j-1
    if k < 0:
        k = 0
    if l < 0:
        l = 0

    arr = [D[k,l], D[i,l] , D[k,j]]
    min_val = 100
    min_idx = 0
    for m in range(len(arr)):
        if arr[m] < min_val:
            min_val = arr[m]
            min_idx = m
    if min_idx == 0:
        return k,l
    elif min_idx == 2:
        return k,j
    else:
        return i,l

def output_alignment(D,i,j,s,t,cost):
    k = i-1
    l = j-1
    if i-1 <0:
        k = 0
    if j-1 <0:
        l = 0

    if i == 0 and j==0:
        return cost
    if back_track(D,i,j) == (k,j):
        i=k
        cost += 1 
        return output_alignment(D,i,j,s,t,cost)
    elif back_track(D,i,j) == (i,l):

        j=l
        cost += 1 
        return output_alignment(D,i,j,s,t,cost)
    else:
        i=k
        j=l
        if s[i] != t[j]:
            cost += 1 
        return output_alignment(D,i,j,s,t,cost)


if __name__ == "__main__":
    print(edit_distance(input(), input()))
