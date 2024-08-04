'''
General:
- Technique to deal with overlapping intervals.
- Need to find overlapping interval or merge intervals if they overlap.

6 cases:
1. a and b do not overlap
2. a and b overlap, with b ending after a
3. a completely overlaps b
4. a and b overlap, with a ending after b
5. b completely overlaps a
6. a and b do not overlap
'''

'''
Problem:
Given a list of intervals, merge all the overlapping intervals
to produce a list that has only mutually exclusive intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
'''

