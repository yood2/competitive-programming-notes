# input: string of n chars
# output: length of longest repetition

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