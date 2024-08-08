# if even, x/2
# if odd, x * 3 + 1
# end when n == 1
# eg. n=3, 3>10>5>16>8>4>2>1

n = int(input())
print(n, end = ' ')
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3) + 1
    print(int(n), end = ' ')