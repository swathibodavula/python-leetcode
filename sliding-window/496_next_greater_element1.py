from collections import deque

def next_greater_element(nums1, nums2):
    """Find the next greater element for each element in nums1 based on their positions in nums2.
    We use a monotonic stack to keep track of the next greater elements in nums2.
    Args:
        nums1: List[int] - The first input array.
        nums2: List[int] - The second input array where we find the next greater elements.
    Returns:
        List[int] - A list of next greater elements for each element in nums1. If there is no greater element, return -1 for that element. """

    nums2_dict = {}
    for i in nums2:
        nums2_dict[i] = -1

    dq = deque()
    result = []

    for i in range(len(nums2)):
        while dq and nums2[i] > nums2[dq[-1]]:
            nums2_dict[nums2[dq.pop()]] = nums2[i]
        dq.append(i)

    
    for i in nums1:
        result.append(nums2_dict[i])

    return result

if __name__ == "__main__":
    print(next_greater_element([2, 1, 4], [1, 2, 3, 4]))
    print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
    print(next_greater_element([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
    print(next_greater_element([1, 2, 3], [3, 2, 1]))
    print(next_greater_element([1, 2, 3], [1, 2, 3]))
    print(next_greater_element([6], [6, 1, 2, 3, 7]))
    print(next_greater_element([2, 1, 3], [2, 1, 3]))
    print(next_greater_element([1], [1]))
    print(next_greater_element([2, 4, 1], [1, 3, 4, 2]))
    print(next_greater_element([5, 4, 3], [5, 4, 3, 8]))
                                                                                                                                                