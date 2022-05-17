# python3
import numpy as np
import math

def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

class Heap_h:
    def __init__(self,data=[]):
        self.H = data  
        self.size = len(data)
        self.swaps = []
    def parent(self,i):
        return int((i-1)/2)
    
    def leftchild(self,i):
        return 2*i+1
    
    def rightchild(self,i):
        return 2*i+2
    
    def sift_up(self,i):
        idx = self.parent(i)
        while i>0 and self.H[idx] < self.H[i]:
            self.H[idx],self.H[i] = self.H[i], self.H[idx]
            # print("sift up", i,idx)
            self.swaps.append(idx,i)
            i = idx
            idx = self.parent(i)
    
    def sift_down(self,i):
        
        minIndex = i
        
        l = self.leftchild(i)
        r = self.rightchild(i)
        if r < len(self.H) :
            if r <= self.size and self.H[r] < self.H[minIndex]:
                minIndex = r
        if l < len(self.H) :
            if l <= self.size and self.H[l] < self.H[minIndex]:
                minIndex = l
        if i != minIndex:
            self.H[i] , self.H[minIndex] = self.H[minIndex], self.H[i]
            self.swaps.append([i,minIndex])
            # print("sift down", i,minIndex)
            self.sift_down(minIndex)
            
    def Insert(self,p):
        self.size += 1
        self.H[self.size] = p
        self.sift_up(self.size)
    
    def ExtractMax(self):
        result = self.H[0]
        self.H[0] = self.H[self.size]
        self.size -= 1
        self.sift_down(0)
        
        return result
    
    def Remove(self,i):
        self.H[i] = np.nan
        self.sift_up(i)
        self.ExtractMax()
    
    def ChangePriority(self,i,p):
        old_p = self.H[i]
        self.H[i] = p
        if p<old_p:
            self.sift_up(i)
        else:
            self.sift_down(i)
            
    
    def build_heap(self):
        for i in range(int(math.log(self.size,2))+1,0,-1):
            self.sift_down(i)
            
        """Build a heap from ``data`` inplace.

        Returns a sequence of swaps performed by the algorithm.
        """
        # The following naive implementation just sorts the given sequence
        # using selection sort algorithm and saves the resulting sequence
        # of swaps. This turns the given array into a heap, but in the worst
        # case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        size = self.size
        for i in range(1,len(self.H)-1):
            #self.H[i],self.H[size-1] = self.H[size-1],self.H[i]
            size -= 1
            self.sift_down(0)
            
        return self.swaps
        

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    
    h_ = Heap_h(data)
    
    swaps = h_.build_heap()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    
    h_ = Heap_h(data)
    
    swaps = h_.build_heap()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

