"""
Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays. Hint: Let's assume the intervals are sorted by the interval start time.
Example 1
Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
Output: [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]


Example 2
Input: [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]
Output:[[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]]
"""


def merge(intervals):
    # intervals.sort(key=lambda pair: pair[0])
    res = []
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1] if output else end
            
        if output and start <= lastEnd:
            output.append((start, end))
            # merge
            # output[-1][1] = max(lastEnd, end)
        else:
            res.append(output)
            output = []
    return res


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



    # merged = []
    # minS, maxE = intervals[0][0], intervals[0][1]
    # for interval in intervals:
    #     if not merged or maxE < interval[0]:
    #         merged.append(interval)
    #     else:
    #         # merged[-1][1] = max(merged[-1][1], interval[1])
    #         maxE = max(merged, key=lambda x: x[1])[1]

    # return merged


def merge_intervals2(intervals):
    minS, maxE = intervals[0][0], intervals[0][1]
    res = []
    # for i in range(1, len(intervals)):
    r = 0
    while r < len(intervals):
        temp = []
        # import pdb; pdb.set_trace()
        # if intervals[l][0] >= intervals[r][0] or intervals[l][1] < intervals[r][1]:
        if intervals[r][0] <= minS or intervals[r][0] <= maxE:
            temp.append(intervals[r])
            minS = max(temp, key=lambda x: x[0])[0]
            maxE = max(temp, key=lambda x: x[1])[1]
        res.append(temp)
        r += 1
    return res

    
    # overlapp = []
    # while intervals[i-1][0] >= intervals[i][0] or intervals[i-1][1] < intervals[i][1]:
    #     overlapp.append(intervals[i])
    #     i += 1
    

# Example usage:
intervals2 = [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
intervals = [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]
result = merge_intervals(intervals)
exp2 = [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]
exp = [[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]]
print(result)
assert result == exp
