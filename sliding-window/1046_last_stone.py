import heapq

def last_stone_weight(stones: list[int]) -> int:
    """Python's heapq is a min-heap, so we store negated weights to get a
    max-heap. Popping gives us the most negative value, which is the
    heaviest stone. If the two stones differ, the difference goes back
    into the heap (negated again) and competes in later turns.

    Time: O(n log n). Heapify is O(n), and each turn does a constant
    number of O(log n) pops and pushes. There are at most n - 1 turns,
    because every turn removes at least one stone.
    Space: O(n) for the heap.
    """
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        heaviest = -heapq.heappop(max_heap)
        second_heaviest = -heapq.heappop(max_heap)
        if heaviest != second_heaviest:
            heapq.heappush(max_heap, -(heaviest - second_heaviest))
    return -max_heap[0] if max_heap else 0

if __name__ == "__main__":
    print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # 1
    print(last_stone_weight([1]))                  # 1
    print(last_stone_weight([3, 3]))                  # 0

