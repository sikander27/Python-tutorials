''' 
For this challenge, you need to take 2 matrices as an input from the stdin ,
 add them and print the resultant matrix to the stdout.

Read input from STDIN. Print your output to STDOUT
3 3
1 2 3
4 5 6
7 8 9
3 3
2 3 4
5 6 7
7 8 9
 '''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def sk_solution():
    # Dimension of matrix 1
    n, m=map(int,input().split())
    mat1=[]
    # Taking input values for matrix one 
    for i in range(n):
        row = list(map(int, input().split()))
        mat1.append(row)

    # Dimension of matrix 1
    p, q=map(int,input().split())
    mat2=[]
     # Taking input values for matrix one 
    for i in range(p):
        row = list(map(int, input().split()))
        mat2.append(row)
    
    result = [] # EXTRA: If you want to create a result matrix
    for i in range(p):
        row = []
        for j in range(q):
            k= mat1[i][j]+mat2[i][j]
            row.append(k)
            if j == q-1:
                print(k)
            else:
                print(k, end=" ")
        result.append(row)
    # EXTRA: IF YOU WANT TO PRINT THE RESULT MATRIX
    # print('-----------------')
    # print(result)
sk_solution()

'''
All the below code are a part of trial and erro. They will work too but the sk_solution() is the best optimized solution for this question.
'''



def main():
    ax, ay = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))
    
    m_a = [a1,a2,a3]

    bx, by = map(int, input().split())
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))
    b3 = list(map(int, input().split()))
    
    m_b = [b1, b2, b3]
    m = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for i in range(ax):
        for j in range(ay):
            m[i][j] = m_a[i][j] + m_b[i][j]
        
    for i in range(ax):
        for j in range(ay):
            if j == ay-1:
                print(m[i][j])
            else:
                print(m[i][j], end=" ")
        
        
    # print(ax, ay, bx, by)
    # print(m_a[0][0])
    # print(m)
    
 # Write code here 

# main()

# Using List comprehension
def mainList():
    ax, ay = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))
    
    m_a = [a1,a2,a3]

    bx, by = map(int, input().split())
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))
    b3 = list(map(int, input().split()))
    
    m_b = [b1, b2, b3]
  
    result = [[m_a[i][j] + m_b[i][j] for j in range(ay)] for i in range(ax)]

    for r in result:
        for ri in r:
            if ri == r[-1]:
                print(ri)
            else:
                print(ri, end=" ")  
        
# mainList()
# Accurate code with dynamic input
def main():
    a=input().split()
    n=int(a[0])
    m=int(a[1])
    mat1=[]
    for i in range(n):
        row=[]
        row=input().split()
        mat1.append(row)
    b=input().split()
    p=int(b[0])
    q=int(b[1])
    mat2=[]
    for i in range(p):
        row=[]
        row=input().split()
        mat2.append(row)
    for i in range(p):
        for j in range(q):
            k=(int(mat1[i][j])+int(mat2[i][j]))
            if i==(p-1) and j==(q-1):
                print(k,end="")
            elif j == (q-1):
                print(k)
            else:
                print(k,end=' ')

# main()



 