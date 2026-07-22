
"""Compute the top-k most frequent event types over a sliding window."""


def top_k_in_window(events, window_size, k):
    """
    Args:
        events: List of (timestamp, name) tuples in arrival order.
        window_size: Maximum number of events kept in the window.
        k: Number of names to report at each step.

    Returns:
        List of (timestamp, top_k_names) tuples, one per input event."""
    
    sub_window = []
    output = []

    for i in range(len(events)):
        sub_window.append(events[i])
        if len(sub_window) > window_size:
            sub_window.pop(0)
        
        j = 0
        output_dict = {}

        while j<len(sub_window):
            if sub_window[j][1] not in output_dict.keys():
                output_dict[sub_window[j][1]] = 1
            else:
                output_dict[sub_window[j][1]] += 1
            j += 1
        
        y = sorted(output_dict.items(), key=lambda x:(-x[1],x[0]))[:k]
        
        output.append((events[i][0], [item[0] for item in y]))

    return output

if __name__ == '__main__':
    events = [
    (1, "B"),
    (1, "A"),
    (2, "C"),
    (2, "A")
    ]
    window_size = 1
    k = 2
    print(top_k_in_window(events, window_size, k))


        


        


    



