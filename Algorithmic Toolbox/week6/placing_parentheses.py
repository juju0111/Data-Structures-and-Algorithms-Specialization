# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Uses python3
import numpy as np
def insert_(lst,p,insrt):
    for i in insrt:
        lst.insert(p,i)
    return lst

def split_str(d):
    for i in range(len(d)):
        if len(d[i])>1:
            if '+' in d[i]:
                l = d.split('+',1)
                d.pop(i)
                d = insert_(d,i,l.reverse())
                return split_str(d)
            elif '-' in d[i]:
                l = d.split('-',1)
                d.pop(i)
                d = insert_(d,i,l)
                return split_str(l.reverse())
            elif '*' in d[i]:
                l = d.split('*',1)
                d.pop(i)
                d = insert_(d,i,l)
                return split_str(l.reverse())
            else:
                pass
    return d

class get_maximum:
    def __init__(self,digit,oper):
        self.size = len(digit)
        self.digit = digit 
        self.oper = oper
        self.m = np.eye((self.size))
        self.M = np.eye((self.size))
        
        self.min_v = 1000
        self.max_v = -1000
        for c,i in enumerate(self.digit):
            self.m[c,c] = int(i)
            self.M[c,c] = int(i)
        #print(self.M, self.m)
    def MinAndMax(self,i,j):
        min_ = 0
        max_ = 0
        for k in range(i,j):
            v_1 = self.evalt(self.M[i,k], self.M[k+1,j], self.oper[k])
            v_2 = self.evalt(self.M[i,k], self.m[k+1,j], self.oper[k])
            v_3 = self.evalt(self.m[i,k], self.M[k+1,j], self.oper[k])
            v_4 = self.evalt(self.m[i,k], self.m[k+1,j], self.oper[k])
            min_ = min(min_,v_1,v_2,v_3,v_4)
            max_ = max(max_,v_1,v_2,v_3,v_4)
        return min_, max_

    def evalt(self,a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

    def get_maximum_value(self):
        #write your code here
        for s in range(self.size):
            for i in range(self.size-s):
                j = i+s
                if i==j:
                    x=[self.m[i,i], self.M[i,i]]
                else:
                    x = self.MinAndMax(i,j)

                self.m[i,j] = x[0]
                self.M[i,j] = x[1]
                
        return self.M[0,self.size-1]

    



if __name__ == "__main__":
    in_ = list(input())
    #in_ = list("5-8+7*4-8+9")
    seq = split_str(in_)

    digits = seq[::2]
    oper = seq[1::2]

    gv = get_maximum(digits,oper)
    print(int(gv.get_maximum_value()))
