from collections import defaultdict

def match_streams(stream_a, stream_b, max_delay):

    """Pair up events from two streams that share a key and occur close in time.
    Each stream is a list of (key, timestamp) events. Two events match when they
    share the same key and their timestamps differ by at most max_delay
    Args:
        stream_a: List of (key, timestamp) tuples for the first stream.
        stream_b: List of (key, timestamp) tuples for the second stream.
        max_delay: Maximum allowed absolute difference between two timestamps
            for them to count as a match.

    Returns:
        A tuple ``(matched, unmatched_a, unmatched_b)`` where:
            - ``matched`` is a list of (key, ts_a, ts_b) for each paired event.
            - ``unmatched_a`` is a list of (key, ts) from stream A with no partner.
            - ``unmatched_b`` is a list of (key, ts) from stream B with no partner."""

    stream_a, stream_b = defaultdict(list), defaultdict(list)
    for key, ts in stream_a: stream_a[key].append(ts)
    for key, ts in stream_b: stream_b[key].append(ts)

    matched, unmatched_a, unmatched_b = [], [], []

    for key in stream_a.keys() | stream_b.keys():
        a = sorted(stream_a[key])
        b = sorted(stream_b[key])
        i = j = 0

        while i < len(a) and j < len(b):
            if abs(a[i] - b[j]) <= max_delay:
                matched.append((key, a[i], b[j]))
                i += 1
                j += 1
            elif a[i] < b[j]:
                unmatched_a.append((key, a[i]))
                i += 1
            else:
                unmatched_b.append((key, b[j]))
                j += 1

        for ts in a[i:]:
            unmatched_a.append((key, ts))
        for ts in b[j:]:
            unmatched_b.append((key, ts))

    return matched, unmatched_a, unmatched_b

if __name__ == "__main__":
    stream_a = [
    ("A", 10),
    ("B", 15),
    ("C", 25)]

    stream_b = [
        ("A", 12),
        ("C", 26)
    ]

    max_delay = 2
    matched, unmatched_a, unmatched_b = match_streams(stream_a, stream_b, max_delay)
    print("Matched:", matched)
    print("Unmatched A:", unmatched_a)
    print("Unmatched B:", unmatched_b)