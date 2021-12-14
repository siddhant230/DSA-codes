"""
Problem statement
Design a stack that supports getMin() in O(1) time and O(1) extra space
link : https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

Complexity analysis

TIME : O(1)
SPACE : O(1)
"""


class minStackWithExtraSpace:
    def __init__(self):
        self.stack = []
        self.min_value = 0

    @staticmethod
    def is_empty(array):
        return not len(array)

    def push(self, value):
        if self.is_empty(self.stack):
            self.stack.append(value)
            self.min_value = value
        else:
            if value < self.min_value:
                flag_value = 2 * value - self.min_value
                self.stack.append(flag_value)
                self.min_value = value
            else:
                self.stack.append(value)

    def pop(self):
        # both will get empty together as first element is smallest for one instance
        if self.is_empty(self.stack):
            return
        else:
            popped_element = self.stack.pop(-1)
            if popped_element < self.min_value:
                prev_min_value = 2 * self.min_value - popped_element
                self.min_value = prev_min_value

    def top(self):
        if self.is_empty(self.stack):
            return -1
        else:
            return self.stack[-1]

    def get_min(self):
        return self.min_value


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
