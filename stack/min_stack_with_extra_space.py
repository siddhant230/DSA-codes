"""
Problem statement
Design a stack that supports getMin() in O(1) time and O(N) extra space
link : https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/

Complexity analysis

TIME : O(1)
SPACE : O(N)
"""


class minStackWithExtraSpace:
    def __init__(self):
        self.stack = []
        self.helper = []

    @staticmethod
    def is_empty(array):
        return not len(array)

    def push(self, value):
        if self.is_empty(self.stack):
            self.helper.append(value)
        else:
            if value < self.helper[-1]:
                self.helper.append(value)
        self.stack.append(value)

    def pop(self):
        # both will get empty together as first element is smallest for one instance
        if self.is_empty(self.stack):
            return
        else:
            if self.stack[-1] <= self.helper[-1]:
                self.helper.pop(-1)
            self.stack.pop(-1)

    def top(self):
        if self.is_empty(self.stack):
            return -1
        else:
            return self.stack[-1]

    def get_min(self):
        if self.is_empty(self.helper):
            return -1
        else:
            return self.helper[-1]


if __name__ == "__main__":
    stack = minStackWithExtraSpace()
    stack.push(3)
    stack.push(5)
    print(stack.get_min())
    stack.push(2)
    stack.push(1)
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())
