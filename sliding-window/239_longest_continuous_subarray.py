from collections import deque


def longestSubarray(nums, limit):
    """Find the longest subarray where the absolute difference between any two elements is at most limit.
    Arguments:
        nums: List of integers.
        limit: Integer limit for the absolute difference.
    Returns:
        Length of the longest subarray satisfying the condition.
    """
    max_deque = deque()
    min_deque = deque()

    left = 0
    max_length = 0

    for right in range(len(nums)):
        while max_deque and nums[max_deque[-1]] < nums[right]:
            max_deque.pop()
        max_deque.append(right)

        while min_deque and nums[min_deque[-1]] > nums[right]:
            min_deque.pop()
        min_deque.append(right)

        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if max_deque[0] == left:
                max_deque.popleft()
            if min_deque[0] == left:
                min_deque.popleft()
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length

print(longestSubarray([2, 4, 7], 4))
print(longestSubarray([1, 2, 3, 4], 10))
print(longestSubarray([10, 1, 20], 0))
print(longestSubarray([4, 4, 4, 4], 0))
print(longestSubarray([4, 4, 4, 5, 4], 0))
print(longestSubarray([1, 2, 3, 100], 3))

