from collections import defaultdict
import sys


def find_shortest(arr):
    first_index = dict()
    count = defaultdict(int)
    deg = 0
    min_len = sys.maxsize

    for i, num in enumerate(arr):
        count[num] += 1
        if num not in first_index:
            first_index[num] = i

        if count[num] > deg:
            deg = count[num]
            min_len = i - first_index[num] + 1
        elif count[num] == deg:
            min_len = min(min_len, i - first_index[num] + 1)

    return min_len