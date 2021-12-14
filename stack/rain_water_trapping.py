"""
Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Complexity analysis

TIME : 3 * O(N) = O(N)
SPACE : O(N)
"""


def getMaxToLeft(array):
    max_to_left = [array[0]]
    for i in range(1, len(array)):
        max_to_left.append(max(max_to_left[-1], array[i]))
    return max_to_left


def getMaxToRight(array):
    max_to_right = [array[0]]
    for i in range(1, len(array)):
        max_to_right.append(max(max_to_right[-1], array[i]))
    return max_to_right


def rainWaterTrapping(array):
    # step 1: find the maximum length building to left and right
    max_to_left = getMaxToLeft(array)
    max_to_right = getMaxToRight(array)
    total_water_trapped = 0

    # step 2: for each building, get water trapped above it and sum it
    for i in range(len(array)):
        water_on_current = min(max_to_left[i], max_to_right[i]) - array[i]
        total_water_trapped += water_on_current

    return total_water_trapped


if __name__ == '__main__':
    array = [3, 0, 0, 2, 0, 4]
    total_water_trapped = rainWaterTrapping(array)
    print(total_water_trapped)
    # output : 10
