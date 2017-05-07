# Uses python3
# Author: Ashish Sardana
import collections
import sys


def fast_count_segments(starts, ends, points):
    """Fast algorithm for counting segments problem.
    The idea is to set labels for each of the arrays, sort them and apply
    counting of coverage technique.
    Samples:
    >>> fast_count_segments([0, 7], [5, 10], [1, 6, 11])
    [1, 0, 0]
    >>> fast_count_segments([-10], [10], [-100, 100, 0])
    [0, 0, 1]
    >>> fast_count_segments([0, -3, 7], [5, 2, 10], [1, 6])
    [2, 0]
    >>> fast_count_segments([0, 2, 4], [5, 2, 10], [1, 6, 2, 2])
    [1, 1, 2, 2]
    """
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)

    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    for i in ends:
        pairs.append((i, right_label))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    coverage = 0
    for pair in sorted_pairs:
        if pair[1] == left_label:
            coverage += 1
        if pair[1] == right_label:
            coverage -= 1
        if pair[1] == point_label:
            indices = points_map[pair[0]]
            for i in indices:
                count[i] = coverage

    return count


def naive_count_segments(starts, ends, points):
    """Naive algorithm for counting segments problem.
    For each point, scan the list of all segments to check how many of them
    contain this point. The running time of this algorithm is
    O(len(points) * len(starts))
    making it too slow.
    """
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")