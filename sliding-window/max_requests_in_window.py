
"""
Problem: Maximum API Requests in a Time Window
Category: Sliding Window / Two Pointers
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Assumptions:
- Timestamps are sorted in nondecreasing order.
- The window is [start, start + window_size).
- Duplicate timestamps count as separate requests.
"""

def max_requests_in_window(
    timestamps: list[int],
    window_size: int
) -> int:
    if not timestamps:
        return 0

    max_requests = 0
    start = 0

    for end in range(len(timestamps)):
        while timestamps[end] - timestamps[start] >= window_size:
            start += 1

        max_requests = max(max_requests, end - start + 1)

    return max_requests


if __name__ == "__main__":
    assert max_requests_in_window([1, 2, 3, 10, 11, 12, 70], 10) == 4
    assert max_requests_in_window([1, 1, 2, 3, 100], 5) == 4
    assert max_requests_in_window([], 60) == 0
    assert max_requests_in_window([1, 2, 3, 70], 2) == 2
    assert max_requests_in_window([1, 11], 10) == 1


