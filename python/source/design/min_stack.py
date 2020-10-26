import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__list = []
        
    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.__list.append((x, curMin))

    def pop(self) -> None:
        self.__list.pop()

    def top(self) -> int:
        if not self.__list:
            return None
        length = len(self.__list)
        return self.__list[length - 1][0]

    def getMin(self) -> int:
        if not self.__list:
            return None
        length = len(self.__list)
        return self.__list[length - 1][1]

    def print_all(self):
        print(self.__list)


if __name__ == '__main__':
    s = MinStack()
    ans = []
    ans.append(s.push(-2))
    ans.append(s.push(0))
    ans.append(s.push(-3))
    s.print_all()
    ans.append(s.getMin())
    ans.append(s.pop())
    s.print_all()
    ans.append(s.top())
    s.print_all()
    ans.append(s.getMin())
    s.print_all()
    print(ans)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
