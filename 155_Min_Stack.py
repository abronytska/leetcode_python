class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        if not self.minstack or self.minstack[-1] >= x:
            self.minstack.append(x)

        self.stack.append(x)

    def pop(self) -> None:
        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin()) #// return -3
ms.pop()
print(ms.top())    #// return 0
print(ms.getMin()) #// return -2
