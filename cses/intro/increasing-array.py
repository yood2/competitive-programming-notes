# input: n (size of array), array
# output: minimum number of moves
# algo: modify array so increasing,
# increase value of any element by one each move, 
# what is minimum number of moves?

n = int(input())
arr = input().split(' ')
for i in range(len(arr)):
    arr[i] = int(arr[i])

# start from right
moves = 0

for i in range(1, n):
    if arr[i-1] > arr[i]:
        moves += (arr[i-1] - arr[i])
        arr[i] = arr[i-1]
print(moves)