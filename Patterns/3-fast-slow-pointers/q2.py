'''
Problem:
Any number will be called a happy number if,
after repeatedly replacing it with a number equal to
the sum of the square of all of its digits, leads us to number "1".
All other (not-happy) numbers will never reach "1".
Instead, they will be stuck in a cycle of numbers which does not include "1".

Example 1:
Input: 23
Output: true (23 is a happy number)
Explanation: 
- 2^2 + 3^2 = 4 + 9 = 13
- 1^2 + 3^2 = 1 + 9 = 10
- 1^2 + 0^2 = 1 + 0 = 1 (Therefore happy!)
'''

def find_happy_number(num):
    fast = num
    slow = num

    while fast != 1 and slow != 1:
        fast = calculate(calculate(fast))
        slow = calculate(slow)
        if slow == fast:
            return False
    return True

def calculate(num):
    sum = 0
    while (num > 0):
        digit = num % 10
        sum += digit * digit
        num //= 10
    return sum

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

main()