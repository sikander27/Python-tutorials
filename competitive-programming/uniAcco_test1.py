def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_hash = {}
    t_hash = {}
    for i in s:
        s_hash[i] = s_hash.get(i, 0) + 1
    for i in t:
        t_hash[i] = s_hash.get(i, 0) + 1
    return t_hash == s_hash
    if sorted(s) == sorted(t):
        return True
    return False


def zeroMatric(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    pos = []
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                pos.append((i, j))
    
    for p in pos:
        r, c = p
        for i in range(col_len):
            matrix[r][i] = 0
        for i in range(col_len):
            matrix[i][c] = 0

    return matrix
        