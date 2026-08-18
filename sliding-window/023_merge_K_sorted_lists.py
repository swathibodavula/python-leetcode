import heapq

def merge_k_lists(lists):
    """Merge k sorted linked lists and return it as one sorted list.
    heapq is used to efficiently get the smallest element among the heads of the lists. We maintain a min-heap of size k, where k is the number of lists. Each time we pop the smallest element from the heap, we add it to the result and push the next element from the same list into the heap.
    Args:
        lists: List[List[int]] - A list of k sorted linked lists.
    Returns:
        List[int] - A single sorted list containing all elements from the k lists."""
    min_heap = []

    # Initialize the heap with the first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        next_element_index = element_index + 1

        if next_element_index < len(lists[list_index]):
            next_value = lists[list_index][next_element_index]
            heapq.heappush(min_heap, (next_value, list_index, next_element_index))
    return result

if __name__ == "__main__":
    merged_list = merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    print(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
    