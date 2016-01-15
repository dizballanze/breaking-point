import sys
from breaking_point import find_breaking_point


def find_max_subarray_brutforce(a):
    """
    Find maximum sub array of `a`. O(n*n).
    """
    max_sum = -sys.maxsize-1
    for i in range(0, len(a)):
        curr_sum = 0
        for j in range(i, len(a)):
            curr_sum += a[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_indices = (i, j)
    return (max_indices[0], max_indices[1], max_sum)


def _find_mid(a, start, middle, end):
    """ Find max subarray that includes middle point """
    left_sum = -sys.maxsize - 1
    curr_sum = 0
    for i in range(middle, start - 1, -1):
        curr_sum += a[i]
        if curr_sum > left_sum:
            max_left = i
            left_sum = curr_sum
    right_sum = -sys.maxsize - 1
    curr_sum = 0
    for i in range(middle+1, end+1):
        curr_sum += a[i]
        if curr_sum > right_sum:
            max_right = i
            right_sum = curr_sum
    return (max_left, max_right, left_sum + right_sum)


def _divide_rec(a, start, end):
    # Ending case
    if start == end:
        return (start, end, a[start])
    middle = (start + end) // 2
    left_start, left_end, left_sum = _divide_rec(a, start, middle)
    right_start, right_end, right_sum = _divide_rec(a, middle+1, end)
    mid_start, mid_end, mid_sum = _find_mid(a, start, middle, end)
    if left_sum > right_sum and left_sum > mid_sum:
        return (left_start, left_end, left_sum)
    if right_sum > left_sum and right_sum > mid_sum:
        return (right_start, right_end, right_sum)
    return (mid_start, mid_end, mid_sum)


def find_max_subarray(a):
    """
    Find maximum sub array of `a`. O(n*lgn).
    """
    return _divide_rec(a, 0, len(a)-1)


if __name__ == "__main__":
    def input_gen(n):
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] * 4
        return ((a[:n],), dict())
    print(find_breaking_point(find_max_subarray_brutforce, find_max_subarray, input_gen, limit=64, start=2))

