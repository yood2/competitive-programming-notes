# input: string of n chars
# output: length of longest repetition
# eg. input: ATTCGGGA - output: 3

# my solution:
# iterate through string and check if same as prev.
# if same, increment. if not, check longest, change prev.
#####################################################################
# n = input()
# longest = 0
# prev = None
# count = 0
# for c in n:
#     if prev == None:
#         prev = c
#         count += 1
#     elif c == prev:
#         count += 1
#     else:
#         if count > longest:
#             longest = count
#         prev = c
#         count = 1
# if count > longest:
#     longest = count
# print(longest)

# online solution:
#####################################################################
n = input()
longest = 1
count = 1
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count += 1
    else:
        if count > longest:
            longest = count
        count = 1
print(max(longest, count))