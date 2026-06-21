from sortedcontainers import SortedList

class MinStack:

    def __init__(self):
        self.arr = []
        self.sortedList = SortedList()

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.sortedList.add(val)

    def pop(self) -> None:
        val = self.arr.pop()
        self.sortedList.discard(val)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.sortedList[0]
