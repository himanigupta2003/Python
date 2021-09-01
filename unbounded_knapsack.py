from typing import List

""" A naive recursive implementation of 0-1 Knapsack Problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""


def unbounded_knapsack(capacity: int, weights: List[int], values: List[int], counter: int) -> int:
    """
    Returns the maximum value that can be put in a unbounded_knapsack of a capacity,
    whereby each weight has a specific value.

   >>> capacity = 100
    >>> value = [10, 30, 20]
    >>> weight = [5, 10, 15]
    >>> length= len(val)
    >>> unbounded_knapsack(capacity, weight, value, length)
    300

    The result is 300 cause the values of 10 item of 30 got the weight of 300
    which is the limit of the capacity.
    """

    # Base Case
    if counter == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than unbounded_knapsack of capacity,
    #   then this item cannot be included in the optimal solution,
    # else return the maximum of two cases:
    #   (1) nth item included
    #   (2) not included
    if weights[counter - 1] > capacity:
        return unbounded_knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = values[counter - 1] + unbounded_knapsack(left_capacity, weights, values, counter)
        without_new_value = unbounded_knapsack(capacity, weights, values, counter - 1)
        return max(new_value_included, without_new_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
