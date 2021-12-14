"""
we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day,
for which the price of the stock on the current day is less than its price on the given day. 

Complexity analysis

TIME : O(N)
SPACE : O(N)
"""


def stockSpan(array):
    # very similar to nearest greater to left
    span = []
    stack = []

    # step 1: run the loop from left to right
    for i in range(0, len(array)):

        # step 2: pop elements from stack unless find nearest greater stock
        while len(stack):
            if array[stack[-1]] < array[i]:
                stack.pop(-1)
            else:
                break

        # step 3: insert index into span
        if not len(stack):
            span.append(i+1)
        else:
            span.append(i - stack[-1])

        # step 4: push current array index into stack
        stack.append(i)

    return span


if __name__ == "__main__":
    price = [10, 4, 5, 90, 120, 80]
    span = stockSpan(price)
    print(span)
    # output : 1 1 2 4 5 1
