"""Group timestamped user events into sessions."""

def sessionize(events, session_gap):
    """A session is a run of consecutive events from the same user where each
    event falls within `session_gap` of the previous one. A larger gap closes
    the current session and opens a new one for that user.

    Args:
        events: List of (timestamp, user_id) tuples, assumed sorted by
            timestamp ascending.
        session_gap: Maximum allowed gap between consecutive events for them
            to stay in the same session.

    Returns:
        List of (user_id, start_timestamp, end_timestamp, event_count) tuples.
        Sessions closed mid-scan appear in close order, followed by each
        user's final open session in insertion order.

    Time: O(n) — one pass, O(1) dict work per event, plus O(u) to drain.
    Space: O(u) for the active session per user, where u = distinct users."""

    active_sessions = {}
    completed_sessions = []

    for timestamp, user_id in events:
        if user_id not in active_sessions:
            active_sessions[user_id] = [timestamp, timestamp, 1]
        else:
            start_timestamp, end_timestamp, event_count = active_sessions[user_id]

            if timestamp-end_timestamp <= session_gap:
                event_count += 1
                active_sessions[user_id] = [start_timestamp, timestamp, event_count]
            else:
                completed_sessions.append((user_id, start_timestamp, end_timestamp, event_count))

                active_sessions[user_id] = (timestamp, timestamp, 1)


    for user_id, (start_timestamp, end_timestamp, event_count) in active_sessions.items():
        completed_sessions.append((user_id, start_timestamp, end_timestamp, event_count))

    return completed_sessions

if __name__ == "__main__":
    events = [(1, "A"), (2, "B"), (3, "A"), (4, "B"), (10, "A")]
    print(sessionize(events, session_gap=2))



