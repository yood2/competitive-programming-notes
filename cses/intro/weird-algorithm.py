# Input: n
# Output: all values of n during algo
# Algo:
# - if n is even, n/2
# - if n is odd, n*3 + 1

n = int(input())

while n != 1:
    print(n, end=" ")
    if n%2 == 0:
        n = int(n/2)
    else:
        n = int(n*3 + 1)
print(n, end="")