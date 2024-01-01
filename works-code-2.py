"""
There are three integers, x, y, and k, and a given integer n. Initially, x and y are zero, and kis a fixed arbitrary constant.
Perform the following operation that consists of two steps in sequence until n becomes zero.
• Decrease n by k, and increase x by k. If n is less than k, then x is increased by n and n becomes zero
• Decrease n by 20% of its value and add the same to y. If 20% of n is not an integer, then take the greatest integer less than or equal to it, i.e. its floor. Example: 0.99 becomes 0, 1.2 becomes 1.

Find the minimum value of k such that × ≥ y (k
≥ 1) after the above operations are finished on the given integer n.
Example:
n = 100
Given n = 100, Initially we have x = 0, y = 0. It is
optimal to choose k = 7,
1. n = 75, x = 7, y = 18 (x is increased by 7, n is
decreased by 7, n = 93, vis increased by 20% of
ni.e 20% of 93 = 18.6, y = 18, n = 75)
2. n = 55, x = 14, y = 31
3. n = 39, x = 21, y = 40
4. n = 26, x = 28, v = 46
5. n = 16, x = 35, y = 49 (x is increased by 7, n is
decreased by 7, n = 19, y is increased by 20% of
nie 20% of 19 = 3.8, vis increased by 3, n is
decreased by 3. n = 16)
6. n = 8, x = 42, y = 50
7. n = 1, x = 49, v = 50
8. n = 0, x = 50, y = 50 (as n = 1, which is less that k,
xis increased by nie 1, n is reduced to 0)
Hence the answer is 7 and it can be shown that answer cannot be less than 7.
Function Description
Complete the function getMinimum in the editor below.
getMinimum has the following parameter:
int n. given integer
Returns
int the minimum possible value of k
"""
import math

def getMinimum(n):
    x = 0
    y = 0
    k = 1

    while n > 0:
        # Decrease n by k, and increase x by k
        n -= k
        x += k

        if n <= 0:
            break

        # Decrease n by 20% of its value and add the same to y
        y_increment = math.floor(0.2 * n)
        y += y_increment
        n -= y_increment

        k += 1

    return k

# Example usage:
n = 21
result = getMinimum(n)
print(result)
