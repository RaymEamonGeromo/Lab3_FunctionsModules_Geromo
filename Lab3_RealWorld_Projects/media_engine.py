def monitor_stream(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def play_count_stream(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2

def process_media(limit):
    total_plays = 0
    records_processed = 0
    
    print("Streaming media counts...")
    for count in play_count_stream(limit):
        total_plays += count
        records_processed += 1
    
    return total_plays, records_processed