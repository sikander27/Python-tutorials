"""
Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays. Hint: Let's assume the intervals are sorted by the interval start time.
Example 1
Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
Output: [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]


Example 2
Input: [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]
Output:[[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]]

company : Bright Edge
"""



def merge_intervals(intervals):
    res = []
    i = 1
    if not intervals:
        return res

    temp = [intervals[0]]
    lastEnd = temp[0][1]
    while i < len(intervals):
        if intervals[i][0] <= lastEnd:
            temp.append(intervals[i])
        else:
            res.append(temp)
            temp = [intervals[i]]

        i += 1
        lastEnd = max(temp, key=lambda x: x[1])[1]
    res.append(temp)
    return res

# Example usage:
intervals2 = [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
intervals = [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]
result = merge_intervals(intervals)
exp2 = [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]
exp = [[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]]
print(result)
assert result == exp