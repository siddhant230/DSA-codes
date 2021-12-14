"""
Problem Statement
Find the largest rectangular area possible in a given histogram,
where the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit. 

Complexity analysis

TIME : 3 * O(N) = O(N)
SPACE : O(N)
"""


def nearestSmallerIndexToRight(array):
    stack = []
    value = []

    # step 1: Traverse the array from right to left
    for i in range(len(array)-1, -1, -1):

        # step 2: pop elements from stack unless top is smaller than current array element
        while len(stack):
            if array[stack[-1]] >= array[i]:
                stack.pop(-1)
            else:
                break

        # step 3: if stack goes empty, current element is largest, thus push -1.
        if not len(stack):
            value.append(len(array))
        else:
            value.append(stack[-1])

        # step 4: push new element to stack
        stack.append(i)

    # step 5: reverse value array, as we are moving in reverse direction.
    value.reverse()
    return value


def nearestSmallerIndexToLeft(array):
    stack = []
    value = []

    # step 1: Traverse the array from right to left
    for i in range(0, len(array)):

        # step 2: pop elements from stack unless top is smaller than current array element
        while len(stack):
            if array[stack[-1]] >= array[i]:
                stack.pop(-1)
            else:
                break

        # step 3: if stack goes empty, current element is largest, thus push -1.
        if not len(stack):
            value.append(-1)
        else:
            value.append(stack[-1])

        # step 4: push new element to stack
        stack.append(i)

    return value


def maximumAreaRectangle(array):
    area_array = []
    # step 1: calculate nearest smaller tower to left
    left_towers = nearestSmallerIndexToLeft(array)              # O(N)
    # step 2: calculate nearest smaller tower to right
    right_towers = nearestSmallerIndexToRight(array)            # O(N)

    # step 3: calculate areas by index difference
    for i in range(0, len(array)):                              # O(N)
        area_array.append(array[i] * ((right_towers[i] - left_towers[i])-1))

    # step 4: return max area
    return max(area_array)


if __name__ == '__main__':
    array = [2, 1, 5, 6, 2, 3]
    max_val = maximumAreaRectangle(array)
    print(max_val)
    # output : 10
