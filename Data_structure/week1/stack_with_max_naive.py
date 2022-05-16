#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_n = -10000000
    def Push(self, a):
        if a > self.max_n:
            self.max_n = a
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] == self.max_n:
            self.max_n = max(self.__stack[:-1])
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max_n


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    # num_queries = int(input())
    
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        # query = input().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
