import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    """Find the kth largest element in an array.
    A simple approach is to use a min-heap of size k. We iterate through the array and maintain the heap with the k largest elements seen so far. The root of the heap will be the kth largest element.
    Args:
        nums: List[int] - The input array.
        k: int - The kth largest element to find.
    Returns:
        int - The kth largest element in the array."""
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], k = 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 ))
