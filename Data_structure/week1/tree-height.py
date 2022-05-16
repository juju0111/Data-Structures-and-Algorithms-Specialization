# python3

import sys, threading, time
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        
        # Replaced
        def compute_height(self):
                par_idx = []
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        if self.parent[i] in par_idx:
                            continue
                        else:
                            while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;


        def compute_height2(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                            height += 1
                            i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;


def main():
  tree = TreeHeight()
  tree.read()
  #t = time.time()
  print(tree.compute_height())
  #print(time.time() - t)
  
threading.Thread(target=main).start()
