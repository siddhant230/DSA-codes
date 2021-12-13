"""
Problem statement

Given an array, print the Next Greater Element (NGE) for every element to right. 
The Next greater Element for an element x is the first greater element on the right side of x in the array.
Elements for which no greater element exist, consider the next greater element as -1. 

Complexity analysis

TIME : O(N)
SPACE : O(N)
"""


def nearestGreaterToRight(array):
    stack = []
    value = []

    # step 1: Traverse the array from right to left
    for i in range(len(array)-1, -1, -1):

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

    # step 5: reverse value array, as we are moving in reverse direction.
    value.reverse()
    return value


if __name__ == '__main__':
    array = [1, 3, 2, 4, 0, 5]
    value = nearestGreaterToRight(array)
    print(value)
    # output : [3, 4, 4, 5, 5, -1]
