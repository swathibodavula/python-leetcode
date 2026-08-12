def nextGreaterElements(nums):
    """Find the next greater element for each element in a circular array.
    Arguments:
        nums: List of integers.
    Returns:
        List of integers where each element is replaced by the next greater element in the circular array.
        If no greater element exists, replace it with -1."""
    n = len(nums)
    answer = [-1] * n
    stack = []                        # holds indices, heights strictly decreasing

    for i in range(2 * n):
        cur = nums[i % n]
        # while current bar is taller than the bar at stack top,
        # current is that bar's next-greater
        while stack and nums[stack[-1]] < cur:
            answer[stack.pop()] = cur
        # only push real indices during the first pass;
        # second pass is resolve-only
        if i < n:
            stack.append(i)

    return answer
next_greater_elements = nextGreaterElements([1, 2, 1])