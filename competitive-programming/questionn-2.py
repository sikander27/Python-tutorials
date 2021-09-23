# python 3.8
# Input
# 3 4
# 3 5 3
# 7 4 7 -1
# Output
# -1 3 3


def findx(x, y, f=0):
    """
    x = list A
    y = list B
    f = flag to check if y is a subset of x
    """
    print(x)
    print(y)
    for i in range(len(x)):
        for j in range(len(y)):
            if (x[i] * y[j]) % 9 == 0:
                print(x[i], y[j])
                # if f and j != i-1:
                #     print("inside")
                return list((x.pop(i), x.pop(j-1))) if f else list((x.pop(i), y.pop(j)))

def findz(x):
    print("in z")
    print(x)
    print(x)
    for i in range(0, len(x)-1):
        print("inside first loop{}".format(i))
        for j in range(i + 1, len(x)):
            print("inside loop{},{}".format(i,j))
            if (x[i] * x[j]) % 9 == 0:
                print("x=>{}....u=>{}".format(i,j))
                return list((x.pop(i), x.pop(j)))
    return []
            
def findy(x, y):
    for i in range(len(y)):
        if (x[0]*x[1]*y[i]) % 9 == 0:
            return y.pop(i)


def main():
    pair = []
    m, n =map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) + len(B) < 3:
        return -1
    A.sort()
    B.sort()
    import pdb; pdb.set_trace()
    pair.extend(findz(A))
    if len(pair) < 2:
        pair.extend(findz(B))
    if len(pair) < 2:
        pair.extend(findx(A, B))
    if len(pair) == 2:
        pair.append(findy(pair, A))
    if len(pair) == 2:
        pair.append(findy(pair, B))
    
    print(A)
    print(B)
    if len(pair) < 3:
        return -1
    return " ".join(map(str,pair))


result = main()
print(result)

