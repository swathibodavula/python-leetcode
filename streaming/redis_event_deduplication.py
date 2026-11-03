"""
Redis Event Deduplication
Topic: Hashing, ttl, Idempotency.
"""
import fakeredis

TTL_SECONDS = 600

redis_client = fakeredis.FakeRedis(decode_responses=True)

def is_new_event(event_id: str) -> bool:
    """
    Check if the event is new (not seen before) and store it in Redis with a TTL.
    If the event is already present, return False. Otherwise, return True.
    """
    # Use SETNX to set the key only if it does not already exist
    result = redis_client.set(name= f"event:{event_id}", value="seen", nx=True, ex=TTL_SECONDS)
    return result is True

def main():
    events = [
        {"event_id": "E101", "amount": 500},
        {"event_id": "E102", "amount": 200},
        {"event_id": "E101", "amount": 500},
    ]

    expected = [True, True, False]

    for event, expected_result in zip(events, expected):
        result = is_new_event(event["event_id"])
        assert result == expected_result
        print(f"{event['event_id']}: {'NEW' if result else 'DUPLICATE'}")


if __name__ == "__main__":
    main()
