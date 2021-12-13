"""
Problem statement
Given an array, print the Next Smaller Element (NSE) for every element to left. 
The Next smaller Element for an element x is the first smaller element on the left side of x in the array.
Elements for which no smaller element exist, consider the next snmaller element as -1. 

Complexity analysis

TIME : O(N)
SPACE : O(N)
"""


def nearestSmallerToLeft(array):
    stack = []
    value = []

    # step 1: Traverse the array from left to right
    for i in range(0, len(array)):

        # step 2: pop elements from stack unless top is smaller than current array element
        while len(stack):
            if stack[-1] > array[i]:
                stack.pop(-1)
            else:
                break

        # step 3: if stack goes empty, current element is smallest, thus push -1.
        if not len(stack):
            value.append(-1)
        else:
            value.append(stack[-1])

        # step 4: push new element to stack
        stack.append(array[i])

    return value


if __name__ == '__main__':
    array = [1, 3, 2, 4, 0, 5]
    value = nearestSmallerToLeft(array)
    print(value)
    # output : [-1, 1, 1, 2, -1, 0]
