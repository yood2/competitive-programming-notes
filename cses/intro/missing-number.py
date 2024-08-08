# input: n, array with numbers 1-n with n-1 numbers
# output: print missing number
# algo: print missing number

n = int(input())
arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

# use bitwise xor
xor = 0
for i in range(1, n+1):
    xor ^= i
for e in arr:
    xor ^= e
print(xor)
