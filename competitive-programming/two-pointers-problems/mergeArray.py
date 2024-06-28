"""
Company interview : Brightedge
"""

def mergeArray(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            a.pop()
            a.insert(i, b[j])
            j += 1
            i += 1
        elif a[i] < b[j]:
            i += 1
    if j < len(b):
        for i in range(len(b)-j):
            a.pop()
        a.extend(b[j:])

    return a


A = [1, 3, 5, 7, 0, 0, 0]
B = [2, 8, 9]
print(mergeArray(A, B))