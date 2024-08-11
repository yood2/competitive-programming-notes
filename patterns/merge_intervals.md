# Merge Intervals
## Summary
An efficient technique to deal with overlapping intervals. Mainly used when we either need to find overlapping intervals or merge them.
## Key Characteristics
- Sort the intervals based on the start time.
- Iterate through the intervals and merge them if they overlap.
- Update the start and end of the merged interval.
- Generally 3 'checks' for merged intervals:
  - Overlap (start of one interval is inside another or end of one interval is inside another)
  - One interval completely inside another (one interval is a subset of another)
  - One interval completely outside another (no overlap)
## General Format
For a list of intervals, we can merge them as follows. The basic idea is that we first sort the intervals based on the start time. Then we iterate through the intervals and merge them if they overlap. If they don't overlap, we add the current interval to the merged list.
```python
#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

def merge(intervals):
    # if only one interval, just return
    if len(intervals) < 2:
        return intervals

    mergedIntervals = []

    # need to sort intervals by start time for this algo to work
    intervals.sort(key=lambda x: x.start)

    # basic idea is we check if current interval end time is greater than next intervals start time.
    # if yes, we combine the intervals (using the max between the two intervals' start times.)
    # if no, add interval to merged, move on to the next interval (since we are assuming it is not overlapping with the rest)
    start = intervals[0].start
    end = intervals[0].end
    for interval in intervals:
        if interval.start <= end:
            # over lap found
            end = max(interval.end, end)
        else:
            # no overlap, add the previous interval to merged list, move on to the next interval
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))

    return mergedIntervals
```
## Inserting a new Interval
Basic idea is to skip all the non-overlapping intervals (we know this since their end is before new intervals start). Then we merge all intervals where start is within new's end. Finally, we add the merged intervals, and add the rest of the intervals.
```python
def insert_interval(intervals, new):
    merged = []
    i = 0
    n = len(intervals)

    # skip all the non overlapping intervals (we know this since their end is before new intervals start)
    while i < n and intervals[i][1] < new[0]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals where start is within new's end
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1

    # add the merged intervals, and add the rest of the intervals
    merged.append(new)
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged
```
