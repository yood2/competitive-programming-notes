# input1: integer n
# input2: n-1 numbers, distinct and between 1 and n
# output: print missing number
# eg. input: 5, [2,3,1,5]
# eg. output: 4

# 1+2+3+4+5 = 15
# 2+3+1+5 = 11
# sum array?

# my solution:
# compare sum of n to sum of inputs. difference is the missing number
#####################################################################
# n = int(input())
# nlist = input()
# nlist = [int(ele) for ele in nlist.split()]
# nsum = (n*(n+1))/2
# listsum = 0
# for i in nlist:
#     listsum += i
# print(int(nsum - listsum))

# bitwise XOR solution
# basically, xor of any number with itself will lead to 0. every number should happen twice. 
# whatever number doesnt repeat is the missing number.
#####################################################################
n = int(input())
nlist = input()
nlist = [int(ele) for ele in nlist.split()]
xor = 0
for i in range(n-1):
    xor ^= nlist[i]
    xor ^= (i + 1)
xor ^= n
print(xor)