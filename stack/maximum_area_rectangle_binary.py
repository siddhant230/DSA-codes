"""
Problem Statement
Find the largest rectangular area possible in a given binary histogram matrix,
where the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit. 

Complexity analysis

TIME : O(R*C)
SPACE : O(N)
"""

from maximum_area_rectangle import maximumAreaRectangle
# maximum_area_rectangle is one of the files in this same repo; under stack


def maximumAreaRectangleBinary(matrix):
    # step 1 : initialize a dummy cumulating floor
    combined_floors = [0 for _ in range(len(matrix[0]))]
    max_areas = 0

    # step 2: for each floor cumulate the floors in a given condition
    for i in range(len(matrix)):                                        # O(R)

        for j in range(len(matrix[0])):                                 # O(C)
            if matrix[i][j] == 0:
                combined_floors[j] = 0
            else:
                combined_floors[j] += matrix[i][j]
        # step 3: find maximum area for each floor
        max_area_per_floor = maximumAreaRectangle(combined_floors)      # O(C)
        max_areas = max(max_areas, max_area_per_floor)                  # O(C)

    return max_areas


if __name__ == '__main__':
    matrix = [[0, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 0, 0]]

    max_area_value = maximumAreaRectangleBinary(matrix)
    print(max_area_value)
    # output : 8
