import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Find the k most frequent elements in a list of integers.
    
    Args:
        nums: A list of integers.
        k: The number of most frequent elements to return.
    
    Returns:
        A list of the k most frequent elements.
    """
    count = Counter(nums)

    heap= []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([1], 1))
    print(top_k_frequent([1, 2], 2))
    print(top_k_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))