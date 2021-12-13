"""
Problem statement
Given an array, print the Next Greater Element (NGE) for every element to left. 
The Next greater Element for an element x is the first greater element on the left side of x in the array.
Elements for which no greater element exist, consider the next greater element as -1. 

Complexity analysis

TIME : O(N)
SPACE : O(N)
"""


def nearestGreaterToLeft(array):
    stack = []
    value = []

    # step 1: Traverse the array from left to right
    for i in range(0, len(array)):

        # step 2: pop elements from stack unless top is greater than current array element
        while len(stack):
            if stack[-1] < array[i]:
                stack.pop(-1)
            else:
                break

        # step 3: if stack goes empty, current element is largest, thus push -1.
        if not len(stack):
            value.append(-1)
        else:
            value.append(stack[-1])

        # step 4: push new element to stack
        stack.append(array[i])

    return value


if __name__ == '__main__':
    array = [1, 3, 2, 4, 0, 5]
    value = nearestGreaterToLeft(array)
    print(value)
    # output : [-1, -1, 3, -1, 4, -1]
