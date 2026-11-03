"""
Problem: Merge Overlapping Intervals
Category: Sorting / Intervals
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Sort intervals by start time.
2. Merge overlapping or touching intervals.
3. Preserve the original input.
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # sort the intervals by their start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = sorted_intervals[0].copy()
    output = []

    for current in sorted_intervals[1:]:
        #if the current interval overlaps with the merged interval, merge them.
        if current[0] <= merged[1]:
            merged[1] = max(merged[1], current[1])

        else:
            output.append(merged)
            merged = current.copy()

    output.append(merged)
    return output

if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 18]]) == [[1, 6], [8, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 10], [2, 3], [4, 8]]) == [[1, 10]]
    assert merge_intervals([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]
    assert merge_intervals([]) == []
