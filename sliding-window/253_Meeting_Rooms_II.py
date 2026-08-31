import heapq
from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    ordered = sorted(intervals, key= lambda meeting: meeting[0])

    active_rooms = []

    for start, end in ordered:
        if active_rooms and active_rooms[0] <= start:
            heapq.heappop(active_rooms)
        heapq.heappush(active_rooms, end)
    return len(active_rooms)

if __name__ == '__main__':
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 5]]) == 1
    assert min_meeting_rooms([[1, 3], [2, 4], [5, 10], [6, 11]]) == 2


