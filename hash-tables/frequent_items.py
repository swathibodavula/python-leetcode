"""Return the k most frequently occurring items."""

def frequent_items(events, k):
    """
    Args:
        events: List of items.
        k: Number of top items to return. Assumed 0 <= k <= number of
            distinct items in `events`.

    Returns:
        List of the k most frequent items, ordered most frequent first.
        Ties are broken arbitrarily (by whatever order `sorted` happens
        to produce for equal counts).

    Time: O(n + m log m) — n to count, m log m to sort, where m = distinct items.
    Space: O(m) for the count dict."""

    output = {}
    result = []

    for event in events:
        if event not in output.keys():
            output[event] = 0
        
        output[event]+=1


    data_sort = sorted(output.items(), key=lambda x:x[1], reverse=True)

    for j in range(k):
        result.append(data_sort[j][0])

    return result


if __name__ == '__main__':

    events = [
    "a",
    "b",
    "a",
    "c",
    "b",
    "b"
    ]
    k = 2
    frequent_items(events, k)

