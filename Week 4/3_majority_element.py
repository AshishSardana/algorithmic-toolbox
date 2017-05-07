# Uses python3
# Author: Ashish Sardana
import sys


def get_majority_element(a, left, right):
    """Majority Element.
    An element of a sequence of length n is called a majority element if
    it appears in the sequence strictly more than n/2 times.
    Samples:
    >>> n = 5; a = [2, 3, 9, 2, 2]
    >>> get_majority_element(a, 0, n)
    1
    >>> # Explanation: 2 is the majority element.
    >>> n = 4; a = [1, 2, 3, 4]
    >>> get_majority_element(a, 0, n)
    0
    >>> # Explanation: There is no majority element in this sequence.
    >>> n = 4; a = [1, 2, 3, 1]
    >>> get_majority_element(a, 0, n)
    0
    >>> # Explanation: This sequence also does not have a majority element.
    >>> # (note that the element 1 appears twice and hence is not
    >>> # a majority element).
    """

    # The task is solved using Boyer–Moore majority vote algorithm.

    maj_index = 0
    count = 1
    for i in range(1, right):

        if a[i] == a[maj_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    count = 0
    for i in range(right):
        if a[i] == a[maj_index]:
            count += 1

    if count > right // 2:
        return a[maj_index]
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)