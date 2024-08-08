# input1: integer n
# input2: n-1 numbers, distinct and between 1 and n
# output: print missing number
# eg. input: 5, [2,3,1,5]
# eg. output: 4

# 1+2+3+4+5 = 15
# 2+3+1+5 = 11
# sum array?

n = int(input())
nlist = input()

res = [int(ele) for ele in nlist.split()]

nsum = 0
listsum = 0

for i in range(n+1):
    nsum += i

for i in res:
    listsum += i

final = nsum - listsum

print(final)